from create_db_for_ng import get_config
# nzb_from_sqlite_xml.py
import sqlite3, re, time
import xml.etree.ElementTree as ET
from datetime import datetime
import xml.dom.minidom as minidom
import re
config = get_config()
DEBUG = config['debug']['DEBUG']

# ---------- normalizers & parsers ----------

LEADING_SET_PREFIX = re.compile(
    r"^\s*(?:\[\s*\d+\s*/\s*\d+\s*\]\s*[-–:]*\s*)", re.IGNORECASE
)

COUNTER_RE = re.compile(
    r"""(?:\byenc\b\s*)?[\(\[\{]\s*(\d+)\s*[/ ]\s*(\d+)\s*[\)\]\}]""",
    re.IGNORECASE | re.VERBOSE,
)
PART_N_OF_M_RE = re.compile(r"\bpart\s*(\d+)\s*of\s*(\d+)\b", re.IGNORECASE)

def normalize_subject_base(subject: str) -> str:
    s = subject or ""
    # drop leading collection index like "[01/37] - "
    s = LEADING_SET_PREFIX.sub("", s)
    # remove ALL counters (n/m and "part n of m")
    s = COUNTER_RE.sub("", s)
    s = PART_N_OF_M_RE.sub("", s)
    # clean common noise
    s = re.sub(r"\byenc\b", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s{2,}", " ", s).strip(" -_.")
    return s

def find_all_counters(subject: str):
    s = subject or ""
    out = []
    for m in COUNTER_RE.finditer(s):
        out.append((int(m.group(1)), int(m.group(2))))
    for m in PART_N_OF_M_RE.finditer(s):
        out.append((int(m.group(1)), int(m.group(2))))
    return out

def extract_segment_counter(subject: str):
    """
    Return (n, m) for the per-file segments by choosing the counter with the smallest m.
    If none found, return (1, 1).
    """
    counters = find_all_counters(subject or "")
    if not counters:
        return (1, 1)
    # choose the smallest m; tie-breaker: smallest n
    counters.sort(key=lambda t: (t[1], t[0]))
    return counters[0]

EMAIL_IN_BRACKETS = re.compile(r"<([^>]+)>")
EMAIL_IN_PARENS   = re.compile(r"\(([^)]+)\)")
def normalize_poster(poster: str) -> str:
    """
    Try to stabilize poster across variations like:
    - "Name <mail@x>" → "mail@x"
    - "mail@x (Name)" → "mail@x"
    - fallback: lowercased, condensed whitespace
    """
    p = poster or "unknown"
    m = EMAIL_IN_BRACKETS.search(p)
    if m:
        return m.group(1).strip().lower()
    # if it looks like "mail@x (Name)"
    if "@" in p and "(" in p and ")" in p:
        # take before first space-paren
        p = p.split(" (", 1)[0]
        return p.strip().lower()
    return re.sub(r"\s{2,}", " ", p.strip()).lower()

import re

# ------------------ subject parsing helpers ------------------

LEADING_SET_PREFIX = re.compile(r"^\s*\[\s*\d+\s*/\s*\d+\s*\]\s*[-–:]*\s*", re.I)
COUNTER_ANY = re.compile(r"""
    (?P<full>(?P<open>[\(\[\{])\s*(?P<n>\d+)\s*[/ ]\s*(?P<m>\d+)\s*(?P<close>[\)\]\}]))
""", re.I | re.VERBOSE)
PART_N_OF_M = re.compile(r"\bpart\s*(?P<n>\d+)\s*of\s*(?P<m>\d+)\b", re.I)

def _find_counters(subject: str):
    s = subject or ""
    out = []
    for m in COUNTER_ANY.finditer(s):
        out.append((m.start(), int(m.group("n")), int(m.group("m"))))
    for m in PART_N_OF_M.finditer(s):
        out.append((m.start(), int(m.group("n")), int(m.group("m"))))
    out.sort(key=lambda t: t[0])  # by position (left → right)
    return out

def extract_nm_leftmost(subject: str):
    counters = _find_counters(subject)
    return (counters[0][1], counters[0][2]) if counters else (1, 1)

def extract_nm_rightmost(subject: str):
    counters = _find_counters(subject)
    return (counters[-1][1], counters[-1][2]) if counters else (1, 1)

def normalize_subject_base(subject: str) -> str:
    s = subject or ""
    s = LEADING_SET_PREFIX.sub("", s)   # drop leading "[x/y] - "
    s = COUNTER_ANY.sub("", s)          # remove (n/m)/[n/m]/{n/m}
    s = PART_N_OF_M.sub("", s)          # remove "part n of m"
    s = re.sub(r"\byenc\b", "", s, flags=re.I)
    s = re.sub(r"\s{2,}", " ", s).strip(" -_.")
    return s

# ------------------ grouping core ------------------

def _group_with_picker(rows, pick_nm, include_poster_in_key=False):
    grouped, singles = {}, []
    for r in rows:
        subj = r["subject"] or ""
        base = normalize_subject_base(subj)
        n, m = pick_nm(subj)

        # normalize or ignore poster; ignoring avoids splits on trivial variations
        poster = (r["from_addr"] or "unknown").strip().lower()
        key = (base, m, poster) if include_poster_in_key else (base, m)

        if m > 1:
            bucket = grouped.setdefault(key, {})
            if n not in bucket or r["artnum"] < bucket[n]["artnum"]:
                bucket[n] = r
        else:
            singles.append(r)

    # scoring: how “good” is this grouping?
    total_grouped_parts = sum(len(segmap) for segmap in grouped.values())
    groups_with_multi = sum(1 for segmap in grouped.values() if len(segmap) >= 2)
    score = (total_grouped_parts, groups_with_multi)
    return grouped, singles, score

def group_rows_auto(rows, include_poster_in_key=False, debug=False):
    # Try RIGHTMOST
    g_r, s_r, score_r = _group_with_picker(rows, extract_nm_rightmost, include_poster_in_key)
    # Try LEFTMOST
    g_l, s_l, score_l = _group_with_picker(rows, extract_nm_leftmost, include_poster_in_key)

    # Choose the one that groups more parts; tie→more groups-with-multi; tie→prefer rightmost
    if score_l > score_r:
        choice = "leftmost"
        grouped, singles, score = g_l, s_l, score_l
    else:
        choice = "rightmost"
        grouped, singles, score = g_r, s_r, score_r

    if debug:
        print(f"[group_rows_auto] choice={choice}  score_left={score_l}  score_right={score_r}")
        # Show a quick summary
        for i, (k, segmap) in enumerate(grouped.items()):
            if i >= 10: break
            print(f"  key={k} parts={sorted(segmap.keys())}")

    return grouped, singles, choice

# ---------------- Subject / parts parsing ----------------

COUNTER_RE = re.compile(
    r"""(?:\byenc\b\s*)?[\(\[\{]\s*(\d+)\s*[/ ]\s*(\d+)\s*[\)\]\}]""",
    re.IGNORECASE | re.VERBOSE,
)
PART_N_OF_M_RE = re.compile(r"\bpart\s*(\d+)\s*of\s*(\d+)\b", re.IGNORECASE)

def _find_all_counters(subject: str):
    s = subject or ""
    out = []
    for m in COUNTER_RE.finditer(s):
        out.append((int(m.group(1)), int(m.group(2)), m.span()))
    for m in PART_N_OF_M_RE.finditer(s):
        out.append((int(m.group(1)), int(m.group(2)), m.span()))
    return out

def _choose_segment_counter(counters):
    # Heuristic: smallest 'm' is the per-file segments counter (e.g. (x/5) vs (x/37))
    return min(counters, key=lambda t: t[1]) if counters else None

def _strip_all_counters(subject: str) -> str:
    s = subject or ""
    s = COUNTER_RE.sub("", s)
    s = PART_N_OF_M_RE.sub("", s)
    s = re.sub(r"\byenc\b", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s{2,}", " ", s).strip(" -_.")
    return s

def parse_subject_for_grouping(subject: str):
    """
    Return (base_subject, seg_n, seg_m).
    base_subject has all counters removed. seg_n/seg_m come from the counter with smallest m.
    """
    counters = _find_all_counters(subject or "")
    pick = _choose_segment_counter(counters)
    base = _strip_all_counters(subject)
    if pick:
        n, m, _ = pick
        return (base or subject or ""), n, m
    return (base or subject or ""), 1, 1

# ---------------- Utilities ----------------

def iso_to_epoch(iso_str: str | None) -> int:
    if not iso_str: return int(time.time())
    try:
        return int(datetime.fromisoformat(iso_str.replace("Z", "+00:00")).timestamp())
    except Exception:
        return int(time.time())

def message_id_text(mid: str) -> str:
    # Normalize to *bare* message-id (no angle brackets)
    if not mid: return ""
    return mid.strip().lstrip("<").rstrip(">")

# ---------------- Main builder ----------------

def build_nzb_filtered(db_path: str, group: str, subject_like: str,
                       from_like: str | None, out_path: str,
                       require_complete_sets: bool = False):
    if not group:
        raise ValueError("group and are required")
    if not subject_like:
        subject_like= " "

    base_like = _strip_all_counters(subject_like) or subject_like

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    where = ["group_name = ?", "subject LIKE ? COLLATE NOCASE"]
    params = [group, f"%{base_like}%"]
    if from_like:
        where.append("from_addr LIKE ? COLLATE NOCASE")
        params.append(f"%{from_like}%")

    cur.execute(f"""
        SELECT message_id, subject, from_addr, date_utc, bytes, artnum, group_name
        FROM articles
        WHERE {' AND '.join(where)}
        ORDER BY artnum
    """, tuple(params))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print(f"No rows for group='{group}', subject~'{base_like}', from~'{from_like or ''}'")
        return

    # Group multipart by (base_without_counters, chosen_m, poster)
    grouped, singles, choice = group_rows_auto(rows, include_poster_in_key=True, debug=False)

    if DEBUG:
        print('printing rows')
        for idx,r in enumerate(rows):
            print(f"{idx} row: {dict(r)}")

        print("printing grouped")
        for idx, (k, segmap) in enumerate(grouped.items()):
            print(f"{idx} key={k} parts={sorted(segmap.keys())}")

        print("printing singles")
        for idx, s in enumerate(singles[:10]):  # preview
            print(f"{idx} single artnum={s['artnum']} subj={s['subject']!r}")

    # Build NZB XML
    nzb = ET.Element("nzb", xmlns="http://www.newzbin.com/DTD/2003/nzb")

    # Multipart
    for (base, m, poster), segmap in grouped.items():
        if require_complete_sets and len(segmap) != m:
            continue

        any_row = next(iter(segmap.values()))
        epochs = [iso_to_epoch(r["date_utc"]) for r in segmap.values() if r["date_utc"]]
        date_epoch = min(epochs) if epochs else iso_to_epoch(any_row["date_utc"])

        file_el = ET.SubElement(nzb, "file", {
            "poster": poster,
            "date": str(date_epoch),
            "subject": f"{base} ({len(segmap)}/{m})",
        })
        groups_el = ET.SubElement(file_el, "groups")
        ET.SubElement(groups_el, "group").text = group

        segs_el = ET.SubElement(file_el, "segments")
        for seg_no in sorted(segmap.keys()):
            r = segmap[seg_no]
            ET.SubElement(segs_el, "segment", {
                "bytes": str(r["bytes"] or 0),
                "number": str(seg_no)
            }).text = message_id_text(r["message_id"])

    # Singles
    for r in singles:
        file_el = ET.SubElement(nzb, "file", {
            "poster": (r["from_addr"] or "unknown").strip(),
            "date": str(iso_to_epoch(r["date_utc"])),
            "subject": (_strip_all_counters(r["subject"]) or "").strip(),
        })
        groups_el = ET.SubElement(file_el, "groups")
        ET.SubElement(groups_el, "group").text = group
        segs_el = ET.SubElement(file_el, "segments")
        ET.SubElement(segs_el, "segment", {
            "bytes": str(r["bytes"] or 0),
            "number": "1"
        }).text = message_id_text(r["message_id"])



    # --- Pretty-print with minidom, then write single-declared NZB ---
    raw = ET.tostring(nzb, encoding="utf-8")              # serialize Element → bytes
    dom = minidom.parseString(raw)                        # parse to DOM
    pretty_str = dom.toprettyxml(indent="  ")             # pretty (returns str, includes its own decl)

    # Strip leading blanks
    lines = pretty_str.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)

    # Remove minidom's XML declaration if present
    if lines and lines[0].lstrip().startswith("<?xml"):
        lines.pop(0)

    # Remove any remaining empty lines at the top (just in case)
    while lines and not lines[0].strip():
        print(lines.pop(0))

    # Join, ensure newline at EOF, and encode to bytes
    pretty_body = ("\n".join(lines) + "\n").encode("utf-8")

    # (Optional) sanity check: body must start with <nzb
    assert pretty_body.lstrip().startswith(b"<nzb"), "Pretty body must start with <nzb>"

    doctype = b'<!DOCTYPE nzb PUBLIC "-//newzBin//DTD NZB 1.0//EN" "http://www.newzbin.com/DTD/nzb/nzb-1.0.dtd">\n'
    with open(out_path, "wb") as f:
        f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')  # single declaration at file start
        f.write(doctype)                                      # DOCTYPE immediately after
        f.write(pretty_body)                                  # pretty-printed body only

    print(f"NZB written: {out_path}  (rows={len(rows)}, multiparts={len(grouped)}, singles={len(singles)})")            


# ---------------- Main  ----------------

if __name__=='__main__':
    subject_filter  = config['filters']['subject']
    from_filter     = config['filters']['from']
    groups          = config['groups']['names'].split(',')
    DB_BASE_PATH    = config['db']['DB_BASE_PATH']
    counter = 1
    for group in groups:
        db_path = f"{DB_BASE_PATH}/{group}.sqlite"
        nzbName = f"{subject_filter.replace('%','_')}_{from_filter.replace('%','_')}_{counter}"
        build_nzb_filtered(db_path, group, subject_like=subject_filter, from_like=from_filter, out_path=f"/mnt/r/tmp/nzbindex/{nzbName}.nzb")