import unittest
from .file_utility import read_file
from typing import List


class TestFileUtility(unittest.TestCase):
    def test_read_file(self):
        test_data_filename: str = 'retrieval/resources/id.stopwords.02.01.2016.txt'
        read_content: str = read_file(test_data_filename)
        self.assertEqual(read_content[:10], 'ada\nadalah')
        read_content: List[str] = read_file(test_data_filename, splitter='\n')
        self.assertEqual(read_content[:2], ['ada', 'adalah'])
        self.assertEqual(len(read_content), 758)


if __name__ == '__main__':
    unittest.main()
