from src.repositories.children_repository import ChildrenRepository
from src.repositories.parents_repository import ParentRepository
from src.repositories.quiz_records_repository import QuizRecordsRepository


class OperateSynonyms:
    @staticmethod
    def insert_to_parents(row: list):
        ParentRepository.insert(row)

    @staticmethod
    def insert_to_children(row: list):
        ChildrenRepository.insert(row)

    @staticmethod
    def insert_to_quiz_records(row: list):
        QuizRecordsRepository.insert(row)