import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.repositories.parents_repository import ParentRepository

ParentRepository.insert(["test1", "noun"])
ParentRepository.insert(["test2", "verb"])
ParentRepository.insert(["test3", "noun"])

parents = ParentRepository.find_by_condition("part_of_speech", "noun")
print(parents)
