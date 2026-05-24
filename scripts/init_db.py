import sqlite3
import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.constants.paths import CHILDREN_SQL_PATH, DB_PATH, PARENTS_SQL_PATH, QUIZ_RECORDS_SQL_PATH

TABLE_DEFINITIONS = (
    CHILDREN_SQL_PATH,
    PARENTS_SQL_PATH,
    QUIZ_RECORDS_SQL_PATH,
)


def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    create_tables(conn)

    conn.commit()
    conn.close()
    

def create_tables(conn):
    for sql_path in TABLE_DEFINITIONS:
        with open(sql_path, encoding="utf-8", newline="") as f_sql:
            conn.executescript(f_sql.read())


if __name__ == "__main__":
    init_db()