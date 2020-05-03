from .preprocessing import Preprocessing
from typing import List


class DataModel:
    def __init__(self, url: str, title: str, img: str, content: str):
        self.__url: str = url
        self.__title: str = title
        self.__img: str = img
        self.__content: str = content
        self.__cleaned: str = Preprocessing.cleaning(Preprocessing.case_folding(title + ' ' + content))
        self.__tokens: List[str] = Preprocessing.tokenizing(self.__cleaned)

    def get_url(self) -> str:
        return self.__url

    def get_title(self) -> str:
        return self.__title

    def get_img(self) -> str:
        return self.__img

    def get_content(self) -> str:
        return self.__content

    def get_cleaned(self) -> str:
        return self.__cleaned

    def get_tokens(self) -> List[str]:
        return self.__tokens
