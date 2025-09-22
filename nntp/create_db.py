from create_db_basic import get_config, upsert_headers,ensure_db, get_nntp_client, TMP_ROWS_PATH_BASE
from email.utils import parsedate_to_datetime
import sqlite3, json
from nntp.headerdict import HeaderDict
from configparser import ConfigParser
import time 


config = get_config()

def clean_text(s: str) -> str:
    return s.encode("utf-8", "ignore").decode("utf-8")

def sanitize_row(row):
    return {k: clean_text(v) if isinstance(v, str) else v for k, v in row.items()}



def to_iso(dt_str: str | None) -> str | None:
    if not dt_str:
        return None
    try:
        return parsedate_to_datetime(dt_str).astimezone(tz=None).isoformat()
    except Exception:
        return None

def row_from_overview(group: str, artnum: int, ov: dict) -> dict:
    # keys can vary in case; normalize lookups
    get = lambda *ks: next((ov[k] for k in ks if k in ov and ov[k] is not None), None)
    msgid = get('Message-ID', 'message-id', 'Message-Id', 'messageid')
    subj  = get('Subject', 'subject')
    frm   = get('From', 'from')
    date  = get('Date', 'date')
    refs  = get('References', 'references', 'Refs', 'refs')
    bytes_ = get('Bytes', 'bytes') or 0
    lines  = get('Lines', 'lines') or 0
    xref   = get('Xref', 'Xref:full', 'xref')

    return sanitize_row({
        "message_id": msgid,
        "group_name": group,
        "artnum": int(artnum),                    # <- guaranteed
        "subject": subj or "",
        "from_addr": frm or "",
        "date_utc": to_iso(date),
        "refs": refs,
        "bytes": int(bytes_),
        "lines": int(lines_ := lines),
        "xref": xref,
    })

def fetch_rows_xzver(nntp_client, group: str, start: int, end: int):
    rows = []
    start_time = time.time()
    cnt, srv_first, srv_last, _ = nntp_client.group(group)    
    for artnum, ov in nntp_client.xover((int(start), int(end))):
        # Skip obviously bad tuples
        if artnum is None or not isinstance(ov, HeaderDict):
            continue
        rows.append(row_from_overview(group, int(artnum), ov))
    end_time = time.time()
    payload_MB = sum(len(str(r).encode("utf-8")) for r in rows)/1_000_000.0      
    mbps =   payload_MB /(end_time - start_time)
    print(f"Retrieved {len(rows):,} from {group}, Elapsed = {end_time - start_time:.4f} seconds at mbps {mbps} ")

    return rows

def fetch_headers_chunked(config:ConfigParser, group:str, limit: int = 5_000_000 , chunk_size: int = 500_000, newest_first: bool = False, start: int = 0, back_filled_up_to:int = -1):
    """
    XZVER-only, chunked.
    - newest_first=True: backfill downward from `start` (or server last) down to max(server first, prev_end+1).
    - newest_first=False: forward incremental from `start` up to server last. (prev_end ignored)
    Assumes: nntp_client.xzver((start,end)) returns the lines directly (bytes/str).

        Args:
        nntp_client: pynntp client (sync)
        group: NNTP group name
        limit: number of headers to fetch (<=0 means "all available")
        chunk_size: max articles per XZVER range (tune if server is touchy)
        newest_first: True → walk ranges from newest to oldest
        start: local db MAX(artnum)
        prev_end : local_db MIN(artnum)

    Returns:
        List[dict]: parsed overview rows
    """

    nntp_client = get_nntp_client(config)
    nntp_client.xfeature_compress_gzip() 

    cnt, srv_first, srv_last, _ = nntp_client.group(group)
    srv_first, srv_last = int(srv_first), int(srv_last)


    print(f"server returned first artnum {srv_first}, last artnum {srv_last} ")
    print(f"server first={srv_first} last={srv_last}")
    print(f"mode={'newest-first' if newest_first else 'forward'}  start={start}  back filled up to ={back_filled_up_to}")
    rows = []
    want = None if (limit is None or limit <= 0) else int(limit)

    if newest_first:
        # Upper bound to start: default to server last; otherwise clamp to server
        # but ingore start completely when backfilling down to the min
        # hi = min(srv_last, int(start) if start and start > 0 else srv_last)
        hi = srv_last
        # Lower bound to stop: do not go below prev_end+1; always respect server first
        low_stop = max(srv_first, (back_filled_up_to + 1) if back_filled_up_to is not None and back_filled_up_to >= 0 else srv_first)

        if hi < low_stop:
            print(f"✅ {group} up to date (local_min={back_filled_up_to}, server_last={srv_last})")
            return []

        # If caller supplied limit, cap theoretical max fetch
        natural = hi - low_stop + 1
        want = natural if (limit is None or limit <= 0) else min(int(limit), natural)
        print(f"computed: hi={hi:,}  lo='n/a'  low_stop={low_stop:,}  want={want:,}")        
        while len(rows) < want and hi >= low_stop:
            end = hi
            start_chunk = max(low_stop, hi - chunk_size + 1)

            # tighten last chunk to not exceed `want`
            remaining = want - len(rows)
            chunk_span = end - start_chunk + 1
            if remaining < chunk_span:
                start_chunk = end - remaining + 1

            # for s in iter_range(start_chunk, end):
            rows.extend(fetch_rows_xzver(nntp_client, group=group,start=start, end=end))
            if len(rows) >= want:
                break
            
            hi = start_chunk - 1
            print(f"retrieved {len(rows):,} out of wanted  {want:,} ")

    else:
        # Oldest-first (forward incremental):
        # `start` should be your local MAX(artnum)+1; clamp to server first.
        lo = max(srv_first, int(start) if start and start > 0 else srv_first)
        if lo > srv_last:
            print(f"✅ {group} up to date (local_max={start-1 if start else 'N/A'}, server_last={srv_last})")
            return []

        natural = srv_last - lo + 1
        want = natural if (limit is None or limit <= 0) else min(int(limit), natural)
        print(f"computed: hi='n/a'  lo={lo} low_stop= 'n/a'  want={want:,}")
        while len(rows) < want and lo <= srv_last:
            start_chunk = lo
            end = min(srv_last, lo + chunk_size - 1)

            # tighten last chunk to not exceed `want`
            remaining = want - len(rows)
            chunk_span = end - start_chunk + 1
            if remaining < chunk_span:
                end = start_chunk + remaining - 1
            print(f"sending request for {group} start:{start_chunk:,} end:{end:,}")                
            rows.extend(fetch_rows_xzver(nntp_client, group=group,start=start_chunk, end=end))
            if len(rows) >= want:
                break

            lo = end + 1
            print(f"retrieved {len(rows):,} out of  {want:,} ")

    return rows


if __name__ == '__main__':
    groups = config['groups']['names'].split(',')    
    DB_BASE_PATH = config['db']['DB_BASE_PATH']

    for group in groups:
        db_path = f"{DB_BASE_PATH}/{group}.sqlite"
        conn = sqlite3.connect(db_path)
        ensure_db(conn)
        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(artnum), 0), COALESCE(MIN(artnum), 0) FROM articles WHERE group_name = ?", (group,))
        local_max, local_min = cur.fetchone()
        print(f'making nntp connection to server with max artnum :{local_max} and min artnum {local_min}')            

        # nntp_client.xfeature_compress_gzip()
        #groups = list(nntp_client.list_active())
        start_time = time.time()
        rows = fetch_headers_chunked(config, group=group, start=local_max, back_filled_up_to = local_min)
        end_time = time.time()
        print(f"Retrieved {len(rows):,} from {group}, Elapsed time for whole group = {end_time - start_time:.4f} seconds")        
        if rows:
            cached_headers_file = f"{TMP_ROWS_PATH_BASE}/{group}.json"
            start_time = time.time()
            with open(cached_headers_file, "w", encoding="utf-8") as f:
                for row in rows:
                    json.dump(row, f, ensure_ascii=False)
                    f.write("\n")
            end_time = time.time()
            print(f"wrote {len(rows):,} to {cached_headers_file} in {end_time - start_time:.4f} seconds")
            start_time = time.time()
            upsert_headers(conn, group, rows)
            end_time = time.time()
            print(f"Upserted {len(rows):,} headers into {db_path} in {end_time - start_time:.4f} seconds")