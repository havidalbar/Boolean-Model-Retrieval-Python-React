import numpy as np
import pickle
import re
from .data_model import DataModel
from .preprocessing import Preprocessing
from typing import Dict, List, Iterable, Set


class BooleanModel:
    def __init__(self, docs_string: str, save_pickle: bool = True, pickle_filename: str = 'boolean_model.pickle'):
        self.__docs: np.ndarray = np.asarray(self.extract_documents(docs_string))
        self.__universal_set: Set[int] = set(range(len(self.__docs)))
        self.indexing()
        boolean_model_file = open(pickle_filename, 'wb')
        pickle.dump(self, boolean_model_file)
        boolean_model_file.close()

    @staticmethod
    def extract_documents(docs_string: str) -> List[DataModel]:
        result: List[DataModel] = []

        def regex_tag(tag_name: str):
            return re.compile(rf'<{tag_name}>(.*?)<\/{tag_name}>', re.DOTALL)

        attribute_tags = [(attribute_tag.lower(), regex_tag(attribute_tag))
                          for attribute_tag in ['URL', 'IMG', 'TITLE', 'CONTENT']]

        for doc in regex_tag('DOC').findall(docs_string):
            new_doc: List[Dict[str, str]] = {}
            for attr_name, attr_regex in attribute_tags:
                new_doc[attr_name] = attr_regex.search(doc).group(1).strip()

            result.append(DataModel(**new_doc))

        return result

    def indexing(self):
        self.__index: Dict[str, Set[int]] = {}
        for doc_index, doc in enumerate(self.__docs):
            for token in set(doc.get_tokens()):
                if self.__index.get(token, None) is None:
                    self.__index[token] = set()
                self.__index[token].add(doc_index)

    def get_indexes(self, token: str) -> Set[int]:
        return self.__index.get(token, set())

    def not_operator(self, token: Set[int]):
        return self.__universal_set.difference(token)

    def get_documents(self, indexes: Iterable, sort_result: bool = True) -> List[DataModel]:
        return [self.__docs[index] for index in (sorted(indexes) if sort_result else indexes)]

    def get_document_by_slug(self, slug: str) -> DataModel:
        for doc in self.__docs:
            if doc.get_slug() == slug:
                return doc

        return None
