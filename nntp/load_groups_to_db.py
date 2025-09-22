# load_groups_sqlite.py
from create_db_basic import get_config, get_nntp_client
import json, time, sqlite3, sys
config = get_config()
from typing import List

import sqlite3, time
from typing import List

def load_groups_jsonl_to_sqlite(groups: List[str], db_path: str):
    """
    Expect lines like: 'comp.lang.python 123456 1 y'
                       (group, last, first, flag)
    We store: group_name, low=first, high=last, status=flag
    """
    now = int(time.time())
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        cur = conn.cursor()

        cur.executescript("""
        CREATE TABLE IF NOT EXISTS nntp_groups (
          group_name TEXT PRIMARY KEY,
          low        INTEGER NOT NULL,
          high       INTEGER NOT NULL,
          status     TEXT NOT NULL CHECK (status IN ('y','n','m','x')),
          updated_at INTEGER NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_groups_prefix ON nntp_groups(group_name);
        """)

        batch: list[tuple] = []
        for line in groups:
            line = line.strip()
            if not line:
                continue
            parts = line.split()  # split on any whitespace
            if len(parts) < 4:
                # skip malformed line
                continue

            group, last_str, first_str, flag = parts[0], parts[1], parts[2], parts[3]

            # Convert to ints; LIST ACTIVE: last=highest, first=lowest
            try:
                high = int(last_str)
                low  = int(first_str)
            except ValueError:
                continue

            # Normalize/validate status
            status = flag.lower()[:1]
            if status not in ("y", "n", "m", "x"):
                status = "x"

            batch.append((group, low, high, status, now))

        if batch:
            cur.executemany("""
                INSERT INTO nntp_groups (group_name, low, high, status, updated_at)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(group_name) DO UPDATE SET
                  low        = excluded.low,
                  high       = excluded.high,
                  status     = excluded.status,
                  updated_at = excluded.updated_at
            """, batch)
            conn.commit()

        print(f"Loaded {len(batch)} groups into {db_path}")
    finally:
        conn.close()



if __name__ == "__main__":
    # usage: python load_groups_sqlite.py groups.jsonl
    DB_BASE_PATH = config['db']['DB_BASE_PATH']
    db_path = f"{DB_BASE_PATH}/groups.sqlite"

    nntp_client = get_nntp_client(config=config)
    groups = list(nntp_client.list())
    load_groups_jsonl_to_sqlite(groups= groups, db_path=db_path )
