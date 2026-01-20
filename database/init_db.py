import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "app.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"

def criar_banco():
    conn = sqlite3.connect(DB_PATH)

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        sql = f.read()

    conn.executescript(sql)
    conn.commit()
    conn.close()

    print("Banco criado com sucesso!")

if __name__ == "__main__":
    criar_banco()
