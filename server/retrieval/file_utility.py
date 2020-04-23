from typing import IO
import os


def read_file(file_path: str, splitter: str = '', encoding: str = 'utf-8'):
    file_pointer: IO = open(file_path, encoding=encoding)
    file_content: str = file_pointer.read()
    file_pointer.close()
    if len(splitter) > 0:
        file_content = file_content.split(splitter)
    return file_content