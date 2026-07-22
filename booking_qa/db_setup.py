import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("test.db")
SCHEMA_PATH = Path(__file__).with_name("schema.sql")
SEED_PATH = Path(__file__).with_name("seed.sql")


def init_db(seed: bool = True) -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        if SCHEMA_PATH.exists():
            conn.executescript(SCHEMA_PATH.read_text())
        if seed and SEED_PATH.exists():
            conn.executescript(SEED_PATH.read_text())
        conn.commit()
        return conn
    except Exception:
        conn.close()
        raise


def get_conn() -> sqlite3.Connection:
    if not DB_PATH.exists():
        init_db(seed=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
