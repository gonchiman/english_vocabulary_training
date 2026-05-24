from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "synonyms.db"

SQL_DIR = BASE_DIR / "sql"
CHILDREN_SQL_PATH = SQL_DIR / "children.sql"
PARENTS_SQL_PATH = SQL_DIR / "parents.sql"
QUIZ_RECORDS_SQL_PATH = SQL_DIR / "quiz_records.sql"