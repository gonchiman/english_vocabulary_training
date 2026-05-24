from src.constants.table_names import TableNames
from src.repositories.repository import Repository


class QuizRecordsRepository(Repository):
    TABLE_NAME = TableNames.QUIZ_RECORDS