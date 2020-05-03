import unittest
from .data_model import DataModel


class TestDataModel(unittest.TestCase):

    def setUp(self):
        self.data_model = DataModel('www.kaskus.com', 'Obat Corona Ampuh', 'img.google.com',
                                    'ini adalah, contoh !@##!@!@#obat corona yang terkenal dan cukup ampuh')

    def test_should_get_url(self):
        self.assertEqual(self.data_model.get_url(), 'www.kaskus.com')

    def test_should_get_img(self):
        self.assertEqual(self.data_model.get_url(), 'www.kaskus.com')

    def test_should_get_title(self):
        self.assertEqual(self.data_model.get_title(), 'Obat Corona Ampuh')

    def test_should_get_raw_text(self):
        self.assertEqual(self.data_model.get_content(),
                         'ini adalah, contoh !@##!@!@#obat corona yang terkenal dan cukup ampuh')

    def test_should_get_cleaned(self):
        self.assertEqual(self.data_model.get_cleaned(),
                         'obat corona ampuh ini adalah contoh obat corona yang terkenal dan cukup ampuh')

    def test_should_get_tokens(self):
        self.assertEqual(self.data_model.get_tokens(),
                         ['obat', 'corona', 'ampuh', 'ini', 'adalah', 'contoh', 'obat',
                          'corona', 'yang', 'terkenal', 'dan', 'cukup', 'ampuh'])


if __name__ == '__main__':
    unittest.main()
