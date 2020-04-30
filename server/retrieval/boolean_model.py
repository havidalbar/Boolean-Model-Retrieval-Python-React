import re
from typing import Dict, List, Set
from retrieval.preprocessing import Preprocessing


class BooleanModel:
    def __init__(self, docs_string: str):
        self.docs = self.__class__.extract_documents(docs_string)
        self.__universal_set: Set[int] = set(range(len(self.docs)))
        self.indexing()

    @staticmethod
    def extract_documents(docs_string: str) -> List[Dict[str, str]]:
        result: List[Dict[str, str]] = []

        def regex_tag(tag_name: str):
            return re.compile(rf'<{tag_name}>(.*?)<\/{tag_name}>', re.DOTALL)

        attribute_tags = [(attribute_tag, regex_tag(attribute_tag))
                          for attribute_tag in ['URL', 'IMG', 'TITLE', 'CONTENT']]

        for doc in regex_tag('DOC').findall(docs_string):
            new_doc = {}
            for attr_name, attr_regex in attribute_tags:
                new_doc[attr_name]: str = attr_regex.search(
                    doc).group(1).strip()

            new_doc['CLEANED']: str = Preprocessing.cleaning(Preprocessing.case_folding(
                f"{new_doc['TITLE']} {new_doc['CONTENT']}"))
            result.append(new_doc)

        return result

    def indexing(self):
        self.index: Dict[str, Set[int]] = {}
        for doc_index, doc in enumerate(self.docs):
            doc_tokens: List[str] = Preprocessing.tokenizing(doc['CLEANED'])

            for token in set(doc_tokens):
                if self.index.get(token, None) is None:
                    self.index[token] = set()
                self.index[token].add(doc_index)

    def get_index(self, token: str):
        return self.index.get(token, set())

    def not_operator(self, token: Set[int]):
        return self.__universal_set.difference(token)
