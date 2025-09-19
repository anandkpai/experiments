import nntp 
import configparser
import sqlite3
from email.utils import parsedate_to_datetime
from email.header import decode_header, make_header
from datetime import timezone
import time
import json
import os
import re
DB_PATH = "/mnt/r/tmp/nzbindex"
TMP_ROWS_PATH_BASE = "/mnt/r/tmp/nzbindex/headers-archive"

def get_config():
    config = configparser.ConfigParser()
    config.read("/mnt/r/tmp/nzbindex/nzbindex.ini")    
    return config 

def get_nntp_client(config:configparser.ConfigParser):
    sconfig = config['servers']
    nntp_client = nntp.NNTPClient( sconfig['host'], sconfig['port'], sconfig['username'], sconfig['password'], use_ssl=True)
    return nntp_client

def ensure_db(conn):
    cur = conn.cursor()
    # Base table to keep all fields (add more columns if your server returns extras)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        message_id   TEXT PRIMARY KEY,
        group_name   TEXT NOT NULL,
        artnum       INTEGER NOT NULL,
        subject      TEXT,
        from_addr    TEXT,
        date_utc     TEXT,          -- ISO8601
        refs         TEXT,
        bytes        INTEGER,
        lines        INTEGER,
        xref         TEXT
    );
    """)
    # FTS5 for fast search (subject/from/message_id); we duplicate minimal fields for simplicity
    cur.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS articles_fts USING fts5(
        subject,
        from_addr,
        message_id,
        group_name,
        artnum UNINDEXED
    );
    """)
    # Helpful indexes
    cur.execute("CREATE INDEX IF NOT EXISTS idx_articles_group_artnum ON articles(group_name, artnum);")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_articles_date ON articles(date_utc);")

    conn.commit()


def _decode_rfc2047(s: str) -> str:
    # Subjects/From may be "=?utf-8?B?...?=" etc.
    try:
        return str(make_header(decode_header(s)))
    except Exception:
        return s

def normalize_date_utc(date_str: str) -> str | None:
    if not date_str:
        return None

    s = date_str.strip()

    # remove RFC-2822 comments: "Tue, 1 Jan 2000 00:00:00 (PST)"
    s = re.sub(r"\([^)]*\)", "", s).strip()

    # common aliases -> numeric offset
    tz_map = {
        "UT": "+0000", "UTC": "+0000", "GMT": "+0000",
    }
    for k, v in tz_map.items():
        # replace standalone tokens only
        s = re.sub(fr"(?<!\S){k}(?!\S)", v, s)

    # 1) try email.utils (handles most RFC-2822 strings)
    try:
        dt = parsedate_to_datetime(s)
        if dt:
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc).isoformat()
    except Exception:
        pass

    # 2) try a few strptime patterns (common NNTP variants)
    patterns = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M %z",
        "%d %b %Y %H:%M %z",
        "%a, %d %b %y %H:%M:%S %z",
        "%d %b %y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S",   # no tz -> assume UTC
        "%d %b %Y %H:%M:%S",
    ]
    for fmt in patterns:
        try:
            dt = datetime.strptime(s, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc).isoformat()
        except Exception:
            continue

    # 3) last resort: if there is a numeric offset without colon like -0500, ensure it’s intact
    # (parsedate_to_datetime already handles this, so this is mostly for badly spaced inputs)
    try:
        # normalize multiple spaces
        s2 = re.sub(r"\s+", " ", s)
        dt = parsedate_to_datetime(s2)
        if dt:
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc).isoformat()
    except Exception:
        pass

    # give up
    return None

def parse_overview_line(line, encoding="utf-8"):
    # Accept bytes or str
    if isinstance(line, (bytes, bytearray)):
        try:
            line = line.decode(encoding, "replace")
        except LookupError:
            line = line.decode("utf-8", "replace")

    parts = line.rstrip("\r\n").split("\t")
    parts += [""] * max(0, 9 - len(parts))

    artnum     = int(parts[0]) if parts[0].isdigit() else None
    subject    = _decode_rfc2047(parts[1])
    from_addr  = _decode_rfc2047(parts[2])
    date_raw   = parts[3]
    message_id = parts[4]
    refs       = parts[5]
    bytes_     = int(parts[6]) if parts[6].isdigit() else None
    lines_     = int(parts[7]) if parts[7].isdigit() else None
    xref       = parts[8]

    # ... keep your date parsing as before ...
    return {
        "message_id": message_id,
        "artnum": artnum,
        "subject": subject,
        "from_addr": from_addr,
        "date_utc": normalize_date_utc(date_raw),  
        "refs": refs,
        "bytes": bytes_,
        "lines": lines_,
        "xref": xref,
    }


def upsert_headers(conn: sqlite3.Connection, group: str, rows: list[dict]):
    # normalize per-row bindings
    to_bind = []
    for r in rows:
        b = r.copy()
        b["group_name"] = group                  # use group_name everywhere
        to_bind.append(b)

    cur = conn.cursor()

    # speed-friendly pragmas for bulk writes
    cur.execute("PRAGMA journal_mode=WAL;")         # once per DB is enough
    cur.execute("PRAGMA synchronous=OFF;")
    cur.execute("PRAGMA temp_store=MEMORY;")
    cur.execute("PRAGMA busy_timeout=5000;")
    cur.execute(f"PRAGMA cache_size=-{512*1024};")  # in KB
    cur.execute("PRAGMA mmap_size=30000000000;")

    cur.execute("BEGIN IMMEDIATE;")  # grab the write lock up front

    start_time = time.time()
    # 1) Upsert base table
    cur.executemany(
        """
        INSERT INTO articles (
            message_id, group_name, artnum, subject, from_addr, date_utc, refs, bytes, lines, xref
        ) VALUES (
            :message_id, :group_name, :artnum, :subject, :from_addr, :date_utc, :refs, :bytes, :lines, :xref
        )
        ON CONFLICT(message_id) DO UPDATE SET
            group_name = excluded.group_name,
            artnum     = excluded.artnum,
            subject    = excluded.subject,
            from_addr  = excluded.from_addr,
            date_utc   = excluded.date_utc,
            refs       = excluded.refs,
            bytes      = excluded.bytes,
            lines      = excluded.lines,
            xref       = excluded.xref;
        """,
        to_bind,
    )


    # TO DO move the fts to a separate process 
    # 2) Stage message_ids we’re refreshing
    cur.execute("DROP TABLE IF EXISTS _tmp_mid;")
    cur.execute("CREATE TEMP TABLE _tmp_mid(message_id TEXT PRIMARY KEY);")
    cur.executemany("INSERT OR IGNORE INTO _tmp_mid(message_id) VALUES(:message_id);", to_bind)

    # 3) ONE delete instead of N deletes
    cur.execute("""
        DELETE FROM articles_fts
        WHERE rowid IN (
            SELECT f.rowid
            FROM articles_fts AS f
            JOIN _tmp_mid AS t ON f.message_id = t.message_id
        );
    """)

    # 4) Bulk insert refreshed rows
    cur.executemany(
        """
        INSERT INTO articles_fts (subject, from_addr, message_id, group_name, artnum)
        VALUES (:subject, :from_addr, :message_id, :group_name, :artnum);
        """,
        to_bind,
    )

    cur.execute("COMMIT;")

    end_time = time.time()    
    cur.execute("PRAGMA synchronous=NORMAL;")

    print(f"wrote to db {len(rows):,} for {group}, Elapsed = {end_time - start_time:.4f} seconds")
    



def fetch_all_headers(nntp_client, group):
    count,first,last,name = nntp_client.group(group)
    print(f"Group: {name}, Articles: {count}, First: {first}, Last: {last}")
    (code, msg) = nntp_client.command(f"XOVER {first}-{last}")
    print(code, msg )
    return [parse_overview_line(ln)  for ln in nntp_client._info(code, msg)]
         



if __name__ == '__main__':
    config = get_config()
    groups = config['groups']['names'].split(',')    
    for group in groups:
        conn = sqlite3.connect(f"{DB_PATH}/{group}.sqlite")
        cached_headers_file = f"{TMP_ROWS_PATH_BASE}/{group}.json"
        if os.path.exists(cached_headers_file):
            with open(cached_headers_file, "r", encoding="utf-8") as f:
                rows = json.load(f)        
            print(f'found {len(rows):,} from {cached_headers_file}')
        else:
            print(f'making nntp connection to server')
            nntp_client = get_nntp_client(config)

            # nntp_client.xfeature_compress_gzip()
            #groups = list(nntp_client.list_active())
            rows = fetch_all_headers(nntp_client, group)
            with open(cached_headers_file, "w", encoding="utf-8") as f:
                json.dump(rows, f, ensure_ascii=False, indent=2)
        ensure_db(conn)
        upsert_headers(conn, group, rows)
    print(f"Upserted {len(rows):,} headers into {DB_PATH}")