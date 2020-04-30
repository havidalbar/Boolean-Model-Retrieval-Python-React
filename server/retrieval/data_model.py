from retrieval.preprocessing import Preprocessing


class DataModel:
    def __init__(self, link: str, title: str, img: str, raw_text: str):
        self.__link: str = link
        self.__title: str = title
        self.__img: str = img
        self.__raw_text: str = raw_text
        self.__cleaned: str = Preprocessing.cleaning(Preprocessing.case_folding(title + ' ' + raw_text))

    def get_link(self) -> str:
        return self.__link

    def get_title(self) -> str:
        return self.__title

    def get_img(self) -> str:
        return self.__img

    def get_raw_text(self) -> str:
        return self.__raw_text

    def get_cleaned(self) -> str:
        return self.__cleaned
