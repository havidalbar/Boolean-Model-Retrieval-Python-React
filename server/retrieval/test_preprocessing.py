import unittest
from .preprocessing import Preprocessing
from typing import List, IO


class TestPreprocessing(unittest.TestCase):
    def test_init(self):
        preprocessing: Preprocessing = Preprocessing()
        self.assertEqual(preprocessing._stopword, set())

        stopword_path: str = 'retrieval/resources/id.stopwords.02.01.2016.txt'
        preprocessing: Preprocessing = Preprocessing(stopword_path)
        stopword_file: IO = open(stopword_path)
        self.assertEqual(preprocessing._stopword, set(
            stopword_file.read().split('\n')))
        stopword_file.close()
        self.assertEqual(len(preprocessing._stopword), 757)

        my_custom_stopword: List[str] = ['dan', 'atau']
        preprocessing: Preprocessing = Preprocessing(my_custom_stopword)
        self.assertEqual(preprocessing._stopword, set(my_custom_stopword))

        self.assertRaises(TypeError, lambda: Preprocessing(10))

    def test_case_folding(self):
        self.assertEqual(Preprocessing.case_folding("KECIL!123"), "kecil!123")
        self.assertEqual(Preprocessing.case_folding("KeCiL!123"), "kecil!123")
        self.assertEqual(Preprocessing.case_folding(
            "BeSaR!123", lower=False), "BESAR!123")
        self.assertEqual(Preprocessing.case_folding(
            "besar!123", lower=False), "BESAR!123")

    def test_cleaning(self):
        self.assertEqual(Preprocessing.cleaning('"terima kasih", pungkasnya.sekian dari saya.'),
                         'terima kasih pungkasnya sekian dari saya')
        self.assertEqual(Preprocessing.cleaning('kekurangan vitamin a. penyakit ini...'),
                         'kekurangan vitamin a penyakit ini')

    def test_filtering(self):
        my_custom_stopword: List[str] = ['dan', 'atau']
        preprocessing: Preprocessing = Preprocessing(my_custom_stopword)
        my_tokens: List[str] = ['saya', 'atau', 'kamu',
                                'akan', 'beli', 'novel', 'dan', 'komik']
        self.assertEqual(preprocessing.filtering(my_tokens), [
                         'saya', 'kamu', 'akan', 'beli', 'novel', 'komik'])

    def test_tokenizing(self):
        my_string: str = 'python  adalah bahasa pemrograman'
        self.assertEqual(Preprocessing.tokenizing(my_string), [
                         'python', 'adalah', 'bahasa', 'pemrograman'])
        self.assertEqual(Preprocessing.tokenizing(my_string, splitter=' '), [
                         'python', '', 'adalah', 'bahasa', 'pemrograman'])
        self.assertEqual(Preprocessing.tokenizing(
            '(demam and panas)', regex_split='\\b\\s*\\b'), ['(', 'demam', 'and', 'panas', ')'])


if __name__ == '__main__':
    unittest.main()
