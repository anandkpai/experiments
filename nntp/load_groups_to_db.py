# load_groups_sqlite.py
from create_db_basic import get_config
import json, time, sqlite3, sys
config = get_config()


def load_groups_jsonl_to_sqlite(jsonl_path: str, db_path: str):
    now = int(time.time())
    conn = sqlite3.connect(db_path)
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

    batch = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            # your keys: group, low, high, status
            batch.append((
                rec["group"],
                int(rec["low"]),
                int(rec["high"]),
                rec["status"],
                now
            ))

    # UPSERT on group_name (SQLite ≥3.24)
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
    conn.close()
    print(f"Loaded {len(batch)} groups into {db_path}")

if __name__ == "__main__":
    # usage: python load_groups_sqlite.py groups.jsonl
    DB_BASE_PATH = config['db']['DB_BASE_PATH']
    db_path = f"{DB_BASE_PATH}/groups.sqlite"
    jsonl_path = f"{DB_BASE_PATH}/groups.jsonl"
    load_groups_jsonl_to_sqlite(jsonl_path=jsonl_path,db_path=db_path )
