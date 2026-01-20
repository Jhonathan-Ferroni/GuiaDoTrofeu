import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # database/
DB_PATH = (BASE_DIR / "app.db").resolve()   # caminho absoluto REAL

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
