import re
from .file_utility import read_file
from typing import IO, Iterable, List, Set


class Preprocessing:
    def __init__(self, stopword=[]):
        if isinstance(stopword, str):
            self._stopword = set(read_file(stopword, splitter='\n'))
        elif isinstance(stopword, Iterable):
            self._stopword = set(stopword)
        else:
            raise TypeError()

    @staticmethod
    def case_folding(input: str, lower: bool = True) -> str:
        if lower:
            return input.lower()
        return input.upper()

    @staticmethod
    def cleaning(input: str, regex_set: str = 'a-z\\s') -> str:
        cleaned: str = re.sub(rf"([{regex_set}]?)([^{regex_set}]+)([{regex_set}]?)", Preprocessing._sub_resolver, input)
        return re.sub(r"\s+", " ", cleaned)

    def filtering(self, tokens: List[str]) -> List[str]:
        return [token for token in tokens if token not in self._stopword]

    @staticmethod
    def tokenizing(input: str, splitter: str = None, regex_split: str = None) -> List[str]:
        if splitter is not None:
            return input.split(splitter)
        if regex_split is not None:
            return list(filter(None, re.split(rf"{regex_split}", input)))
        return input.split()

    @staticmethod
    def _sub_resolver(match: re.Match):
        result = match.group(1)
        if len(match.group(3)) > 0:
            if len(result):
                result += ' '
            result += match.group(3)
        return result
