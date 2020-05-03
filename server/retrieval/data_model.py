from .preprocessing import Preprocessing
from slugify import slugify
from typing import Dict, Iterable, List


class DataModel:
    def __init__(self, url: str, title: str, img: str, content: str):
        self.__url: str = url
        self.__title: str = title
        self.__img: str = img
        self.__content: str = content
        self.__cleaned: str = Preprocessing.cleaning(Preprocessing.case_folding(title + ' ' + content))
        self.__tokens: List[str] = Preprocessing.tokenizing(self.__cleaned)

    def get_slug(self) -> str:
        return slugify(self.__title)

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

    def get_summary(self) -> str:
        split_index: int = 300
        for char_index in range(split_index, 0, -1):
            if self.__cleaned[char_index] == ' ':
                split_index = char_index
                break
        return self.__cleaned[0:split_index] + '…'

    def get_tokens(self) -> List[str]:
        return self.__tokens

    def asdict(self, output_keys: Iterable = ['url', 'title', 'img', 'content']) -> Dict[str, str]:
        converter_dict: Dict[str, str] = {
            'slug': self.get_slug(),
            'url': self.__url,
            'title': self.__title,
            'img': self.__img,
            'content': self.__content,
            'cleaned': self.__cleaned,
            'summary': self.get_summary(),
            'tokens': self.__tokens
        }

        result: Dict[str, str] = {}
        for output_key in output_keys:
            value: str = converter_dict.get(output_key, None)
            if value is not None:
                result[output_key] = value

        return result
