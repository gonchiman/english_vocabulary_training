from src.repositories.children_repository import ChildrenRepository
from src.repositories.parents_repository import ParentRepository


class WordRegistrationService:
    @staticmethod
    def register_multiple_words_to_parents(words: str, part_of_speech: str)-> None:
        word_list = words.replace(' ', '').split(',')
        for word in word_list:
            ParentRepository.insert([word, part_of_speech])

    @staticmethod
    def register_multiple_words_to_children(words: str, parent: str) -> None:
        word_list = words.replace(' ', '').split(',')
        for word in word_list:
            ChildrenRepository.insert([word, parent])