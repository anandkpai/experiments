from create_db_for_ng import DB_PATH
# nzb_from_sqlite_xml.py
import sqlite3, re, time
import xml.etree.ElementTree as ET
from datetime import datetime
import xml.dom.minidom as minidom


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
    if not group or not subject_like:
        raise ValueError("group and subject_like are required")

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
    grouped, singles = {}, []
    for r in rows:
        base, n, m = parse_subject_for_grouping(r["subject"])
        poster = (r["from_addr"] or "unknown").strip()
        if m > 1:
            key = (base, m, poster)
            bucket = grouped.setdefault(key, {})
            # keep earliest artnum per segment number
            if n not in bucket or r["artnum"] < bucket[n]["artnum"]:
                bucket[n] = r
        else:
            singles.append(r)

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
        lines.pop(0)

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

    # # Pretty-print the XML tree in place (Python 3.9+)
    # ET.indent(nzb, space="  ", level=0)
    # # Write: XML declaration + DOCTYPE + root
    # xml_bytes = ET.tostring(nzb, encoding="utf-8")
    # doctype = b'<!DOCTYPE nzb PUBLIC "-//newzBin//DTD NZB 1.0//EN" "http://www.newzbin.com/DTD/nzb/nzb-1.0.dtd">\n'
    # with open(out_path, "wb") as f:
    #     f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
    #     f.write(doctype)
    #     f.write(xml_bytes)

    # print(f"NZB written: {out_path}  (rows={len(rows)}, multiparts={len(grouped)}, singles={len(singles)})")

# ---------------- Example ----------------
# build_nzb_filtered(
#     db_path="data/usenet_headers.sqlite",
#     group="alt.comp",
#     subject_like="Sue Wong's 2010 Fall Collection Preview Event.jpg (1/5) (1/37)",
#     from_like="yum",
#     out_path="sue_wong.nzb",
#     require_complete_sets=False,
# )



if __name__=='__main__':
    group = 'alt.binaries.pictures.teen-starlets'
    subject_filter = r"Bella Thorne%2010"
    from_filter = r"yum"
    nzbName = f"{subject_filter.replace('%','_')}_{from_filter.replace('%','_')}"
    db_path = f"{DB_PATH}{group}.sqlite"
    build_nzb_filtered(db_path, group, subject_like=subject_filter, from_like=from_filter, out_path=f"/mnt/r/tmp/nzbindex/{nzbName}.nzb")