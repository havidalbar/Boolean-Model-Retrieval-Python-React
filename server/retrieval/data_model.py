class DataModel:
    def __init__(self, link: str, title: str, raw_text: str, cleaned: str):
        self.__link: str = link
        self.__title: str = title
        self.__raw_text: str = raw_text
        self.__cleaned: str = cleaned

    def get_link(self) -> str:
        return self.__link

    def get_title(self) -> str:
        return self.__title

    def get_raw_text(self) -> str:
        return self.__raw_text

    def get_cleaned(self) -> str:
        return self.__cleaned
