from src.constants.table_names import TableNames
from src.repositories.repository import Repository


class ParentRepository(Repository):
    TABLE_NAME = TableNames.PARENTS