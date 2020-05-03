import unittest
from .query_processing import infix_to_postfix


class TestQueryProcessing(unittest.TestCase):

    def setUp(self):
        self.expected = ['gatal', 'perih', 'merah', 'or', 'not', 'and']
        self.result = infix_to_postfix('gatal and not (perih or merah)')
        self.expected2 = ['gatal', 'benjolan', 'and', 'perih',
                          'merah', 'or', 'not', 'and', 'demam', 'and']
        self.result2 = infix_to_postfix(
            '(gatal and benjolan) and not (perih or merah) and demam')
        self.expected3 = ['gatal', 'demam', 'panas', 'and',
                          'or', 'perih', 'merah', 'or', 'not', 'and']
        self.result3 = infix_to_postfix(
            '(gatal or (demam and panas)) and not (perih or merah)')

    def test_query1(self):
        self.assertEqual(self.result, self.expected)

    def test_query2(self):
        self.assertEqual(self.result, self.expected)

    def test_query3(self):
        self.assertEqual(self.result, self.expected)


if __name__ == '__main__':
    unittest.main()
