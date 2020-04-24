from retrieval.data_model import DataModel
import unittest


class TestDataModel(unittest.TestCase):

    def setUp(self):
        self.data_model = DataModel('www.kaskus.com', 'Obat Corona Ampuh',
                                    'ini adalah contoh obat corona yang terkenal dan cukup ampuh', 'contoh obat corona terkenal ampuh')

    def test_should_get_link(self):
        self.assertEqual(self.data_model.get_link(), 'www.kaskus.com')

    def test_should_get_title(self):
        self.assertEqual(self.data_model.get_title(), 'Obat Corona Ampuh')

    def test_should_get_raw_text(self):
        self.assertEqual(self.data_model.get_raw_text(),
                         'ini adalah contoh obat corona yang terkenal dan cukup ampuh')

    def test_should_get_cleaned(self):
        self.assertEqual(self.data_model.get_cleaned(),
                         'contoh obat corona terkenal ampuh')


if __name__ == '__main__':
    unittest.main()
