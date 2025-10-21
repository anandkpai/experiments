import os, re, time, xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
import time
from typing import Dict, List, Tuple, Iterable, Any, Optional
from create_db import get_config
config = get_config()
# ------------- Subject parsing / normalization -------------

JPG_RE = re.compile(r'\.(?:jpe?g)(?:\b|$)', re.IGNORECASE)
LEADING_SET_PREFIX = re.compile(r"^\s*\[\s*\d+\s*/\s*\d+\s*\]\s*[-–:]*\s*", re.I)
COUNTER_ANY = re.compile(r"""(?P<full>(?P<open>[\(\[\{])\s*(?P<n>\d+)\s*[/ ]\s*(?P<m>\d+)\s*(?P<close>[\)\]\}]))""", re.I|re.VERBOSE)
PART_N_OF_M = re.compile(r"\bpart\s*(?P<n>\d+)\s*of\s*(?P<m>\d+)\b", re.I)

def _strip_all_counters(subject: str) -> str:
    s = subject or ""
    s = LEADING_SET_PREFIX.sub("", s)
    s = COUNTER_ANY.sub("", s)
    s = PART_N_OF_M.sub("", s)
    s = re.sub(r"\byenc\b", "", s, flags=re.I)
    s = re.sub(r"\s{2,}", " ", s).strip(" -_.")
    return s

def _find_counters(subject: str):
    s = subject or ""
    out = []
    for m in COUNTER_ANY.finditer(s):
        out.append((int(m.group("n")), int(m.group("m"))))
    for m in PART_N_OF_M.finditer(s):
        out.append((int(m.group("n")), int(m.group("m"))))
    return out

def parse_subject_for_grouping(subject: str) -> Tuple[str,int,int]:
    base = _strip_all_counters(subject)
    counters = _find_counters(subject)
    if not counters:
        return base, 1, 1
    n, m = min(counters, key=lambda t: t[1])   # smallest m ≈ per-file parts
    return base, n, m

def normalize_poster(poster: Optional[str]) -> str:
    p = (poster or "unknown").strip()
    m = re.search(r"<([^>]+)>", p)
    if m:
        return m.group(1).lower()
    if "@" in p and "(" in p and ")" in p:
        p = p.split(" (", 1)[0]
    return re.sub(r"\s{2,}", " ", p).lower()

def message_id_text(mid: Optional[str]) -> str:
    return (mid or "").strip().lstrip("<").rstrip(">")

def iso_to_epoch(iso_str: Optional[str]) -> int:
    if not iso_str: return int(time.time())
    try:
        return int(datetime.fromisoformat(iso_str.replace("Z","+00:00")).timestamp())
    except Exception:
        return int(time.time())

# ------------- Lightweight Levenshtein (no deps) -------------

def levenshtein_distance(a: str, b: str) -> int:
    if a == b: return 0
    if not a: return len(b)
    if not b: return len(a)
    if len(a) > len(b): a, b = b, a
    prev = list(range(len(a)+1))
    for j, cb in enumerate(b, 1):
        cur = [j]
        for i, ca in enumerate(a, 1):
            ins = cur[i-1] + 1
            dele = prev[i] + 1
            sub = prev[i-1] + (ca != cb)
            cur.append(min(ins, dele, sub))
        prev = cur
    return prev[-1]

def lev_ratio(a: str, b: str) -> float:
    if not a and not b: return 1.0
    d = levenshtein_distance(a, b)
    return 1.0 - d / max(len(a), len(b))

# ------------- Step 1: rows -> per-JPG file sets -------------

def build_file_sets_from_rows(
    rows: Iterable[Dict[str, Any]],
    only_jpg: bool = True,
    include_poster_in_key: bool = True,
    require_complete_sets: bool = True,
) -> List[Dict[str, Any]]:
    """
    Returns a list of file dicts:
      { 'base', 'poster', 'm', 'segments': {seg_no: row_dict}, 'date_epoch' }
    Each row must have: subject, from_addr, message_id, bytes, artnum, date_utc.
    """
    # Filter & annotate
    annotated = []
    for r in rows:
        subj = r.get("subject") or ""
        base, n, m = parse_subject_for_grouping(subj)
        if only_jpg and not (JPG_RE.search(base) or JPG_RE.search(subj)):
            continue
        rr = dict(r)
        rr["_base"]   = base
        rr["_n"]      = max(1, int(n))
        rr["_m"]      = max(1, int(m))
        rr["_poster"] = normalize_poster(r.get("from_addr") or "")
        annotated.append(rr)

    # Group segments → files (dedupe: keep lowest artnum per seg_no)
    files_map: Dict[Tuple, Dict[int, Dict[str,Any]]] = {}
    for r in annotated:
        key = (r["_base"], r["_m"], r["_poster"]) if include_poster_in_key else (r["_base"], r["_m"])
        bucket = files_map.setdefault(key, {})
        n = r["_n"]
        cur = bucket.get(n)
        if cur is None or (r.get("artnum") is not None and r["artnum"] < cur.get("artnum", 1<<60)):
            bucket[n] = r

    files: List[Dict[str,Any]] = []
    for key, segmap in files_map.items():
        base, m, poster = (key[0], key[1], key[2]) if include_poster_in_key else (key[0], key[1], "unknown")
        if require_complete_sets and len(segmap) != m:
            continue
        any_row = next(iter(segmap.values()))
        epochs = [iso_to_epoch(r.get("date_utc")) for r in segmap.values() if r.get("date_utc")]
        files.append({
            "base": base,
            "poster": poster,
            "m": m,
            "segments": segmap,
            "date_epoch": min(epochs) if epochs else iso_to_epoch(any_row.get("date_utc")),
        })
    return files

# ------------- Step 2: cluster files by subject (per poster) -------------

def normalize_for_similarity(s: str) -> str:
    s = s.lower()
    s = re.sub(r'\.(?:jpe?g)$', '', s)
    s = re.sub(r'[_\-\.\s]+', ' ', s)
    s = re.sub(r'\bimg[_\- ]?\d+\b', 'img', s)
    s = re.sub(r'\d{3,}', '', s)
    return s.strip()

def blocking_key(s: str, key_len: int = 12) -> str:
    s2 = re.sub(r'[\W_]+', '', s)
    s2 = re.sub(r'\d+', '', s2)
    return s2[:key_len]

def cluster_files_by_subject_per_poster(
    files: List[Dict[str,Any]],
    sim_threshold: float = 0.86,
    block_key_len: int = 12,
) -> List[List[Dict[str,Any]]]:
    """
    Clusters files by subject similarity **within each poster** (no mixing posters).
    Greedy clustering within block buckets for speed.
    """
    from collections import defaultdict
    # poster → block → [(norm_base, file)]
    buckets: Dict[str, Dict[str, List[Tuple[str, Dict[str,Any]]]]] = defaultdict(lambda: defaultdict(list))
    for f in files:
        norm = normalize_for_similarity(_strip_all_counters(f["base"]))
        bkey = blocking_key(norm, block_key_len)
        buckets[f["poster"]][bkey].append((norm, f))

    clusters: List[List[Dict[str,Any]]] = []

    items = buckets.items()
    print(f"processing {len(items):,} posters")
    start_time = time.time()
    for count, (poster, by_block) in enumerate(items):        
        for bkey, arr in by_block.items():
            used = [False]*len(arr)
            for i, (norm_i, f_i) in enumerate(arr):
                if used[i]: continue
                cluster = [f_i]
                used[i] = True
                for j, (norm_j, f_j) in enumerate(arr):
                    if used[j]: continue
                    if lev_ratio(norm_i, norm_j) >= sim_threshold:
                        cluster.append(f_j)
                        used[j] = True
                clusters.append(cluster)
                if not(len(clusters)%100) :
                    print(f"created {len(clusters):,} clusters, finished with {count} posters in {time.time() - start_time:4f} seconds")
    print(f"finished: created {len(clusters):,} in {time.time() - start_time:4f}")
    return clusters

# ------------- Step 3: write one NZB per cluster ("album") -------------

def write_album_nzb(
    cluster: List[Dict[str,Any]],
    group_name: str,
    out_dir: str,
    cluster_title: Optional[str] = None
) -> str:
    def common_prefix_str(strings: List[str]) -> str:
        if not strings: return ""
        s1 = min(strings); s2 = max(strings)
        i = 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]: i += 1
        return s1[:i].strip(" -_.")
    bases = [_strip_all_counters(f["base"]) for f in cluster]
    norm_bases = [normalize_for_similarity(b) for b in bases]
    title = cluster_title or (common_prefix_str(norm_bases) or bases[0])

    start_time = time.time()
    nzb = ET.Element("nzb", xmlns="http://www.newzbin.com/DTD/2003/nzb")
    for f in cluster:
        file_el = ET.SubElement(nzb, "file", {
            "poster": f["poster"],
            "date": str(f["date_epoch"]),
            "subject": f["base"],
        })
        groups_el = ET.SubElement(file_el, "groups")
        ET.SubElement(groups_el, "group").text = group_name
        segs_el = ET.SubElement(file_el, "segments")
        for seg_no in sorted(f["segments"].keys()):
            r = f["segments"][seg_no]
            ET.SubElement(segs_el, "segment", {
                "bytes": str(r.get("bytes") or 0),
                "number": str(seg_no),
            }).text = message_id_text(r.get("message_id"))

    raw = ET.tostring(nzb, encoding="utf-8")
    dom = minidom.parseString(raw)
    pretty_str = dom.toprettyxml(indent="  ")
    lines = [ln for ln in pretty_str.splitlines() if ln.strip()]
    if lines and lines[0].startswith("<?xml"):
        lines.pop(0)
    body = ("\n".join(lines) + "\n").encode("utf-8")
    doctype = b'<!DOCTYPE nzb PUBLIC "-//newzBin//DTD NZB 1.0//EN" "http://www.newzbin.com/DTD/nzb/nzb-1.0.dtd">\n'

    safe_title = re.sub(r"[^A-Za-z0-9._-]+", "_", title)[:200] or "album"
    out_path = os.path.join(out_dir, f"{safe_title}__album.nzb")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
        f.write(doctype)
        f.write(body)
    print(f"wrote {out_path} in {time.time()-start_time:.4f} seconds")
    return out_path

def build_album_nzbs_from_rows(
    rows: Iterable[Dict[str,Any]],
    group: str,
    out_dir: str,
    only_jpg: bool = True,
    require_complete_sets: bool = True,
    sim_threshold: float = 0.86,
    block_key_len: int = 12,
    debug: bool = False,
) -> List[str]:
    """
    High-level: rows → file sets → (per-poster) clusters → NZBs.
    Returns list of output paths. Posters are **never** mixed across files in a cluster.
    """
    files = build_file_sets_from_rows(
        rows,
        only_jpg=only_jpg,
        include_poster_in_key=True,          # <= ensures per-poster file keys
        require_complete_sets=require_complete_sets,
    )
    clusters = cluster_files_by_subject_per_poster(
        files, sim_threshold=sim_threshold, block_key_len=block_key_len
    )
    if debug:
        print(f"[albums] files={len(files)} clusters={len(clusters)} "
              f"top_sizes={sorted((len(c) for c in clusters), reverse=True)[:10]}")
    out_paths = [write_album_nzb(cluster, group_name=group, out_dir=out_dir) for cluster in clusters]
    if debug:
        for p in out_paths[:5]:
            print("wrote:", p)
    return out_paths

# ------------- (Optional) helper to read rows from SQLite -------------

def iter_rows_from_sqlite(db_path: str, group: str):
    """
    Yields dicts with the expected fields from your 'articles' table.
    """
    start_time = time.time()
    import sqlite3
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    q = """
    SELECT subject, from_addr, message_id, bytes, artnum, date_utc
    FROM articles
    WHERE group_name = ?
    ORDER BY artnum
    """
    cur = con.execute(q, (group,))
    count = 0
    for r in cur:
        yield dict(r)
        count += 1
    print(f"retrieved {count} rows in {time.time()-start_time:.4f} seconds")
    con.close()
    


if __name__=="__main__":
    DB_BASE_PATH    = config['db']['DB_BASE_PATH']
    group           = config['groups']['names']
    db_path         = f"{DB_BASE_PATH}/{group}.sqlite"       
    out_dir         = f"/mnt/r/tmp/nzbs/{group}"
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    build_album_nzbs_from_rows(iter_rows_from_sqlite(db_path=db_path, group=group),group=group, out_dir=out_dir)