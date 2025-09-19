-- sqlite3 code to read in a previously cached headers file, use the command below, 
-- replace articles.json with the name of the header file
-- sqlite3 mydb.sqlite -cmd ".param set json_file 'articles.json'" ".read load_articles_from_json.sql"


PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

-- 1) Create table (if needed)
CREATE TABLE IF NOT EXISTS articles (
  message_id TEXT PRIMARY KEY,
  group_name TEXT NOT NULL,
  artnum     INTEGER NOT NULL,
  subject    TEXT,
  from_addr  TEXT,
  date_utc   TEXT,     -- keep as ISO-8601 text; convert on query if needed
  refs       TEXT,
  bytes      INTEGER,
  lines      INTEGER,
  xref       TEXT
);

-- Useful index for range & group scans
CREATE INDEX IF NOT EXISTS idx_articles_group_artnum
ON articles(group_name, artnum);

-- 2) Load from a JSON **array** file on disk using readfile()+json_each()
-- Replace 'articles.json' with your file path.
WITH src AS (
  SELECT
    json_extract(value,'$.message_id')           AS message_id,
    json_extract(value,'$.group')                AS group_name,
    CAST(json_extract(value,'$.artnum') AS INT)  AS artnum,
    json_extract(value,'$.subject')              AS subject,
    json_extract(value,'$.from_addr')            AS from_addr,
    json_extract(value,'$.date_utc')             AS date_utc,
    json_extract(value,'$.refs')                 AS refs,
    CAST(json_extract(value,'$.bytes') AS INT)   AS bytes,
    CAST(json_extract(value,'$.lines') AS INT)   AS lines,
    json_extract(value,'$.xref')                 AS xref
  FROM json_each(readfile(':json_file'))
)
INSERT INTO articles (
  message_id, group_name, artnum, subject, from_addr, date_utc, refs, bytes, lines, xref
)
SELECT
  message_id, group_name, artnum, subject, from_addr, date_utc, refs, bytes, lines, xref
FROM src
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
