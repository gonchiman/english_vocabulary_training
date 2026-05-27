import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.repositories.parents_repository import ParentRepository

ParentRepository.insert(["test", "noun"])

parents = ParentRepository.find_values_by_column("word")
print(parents)
