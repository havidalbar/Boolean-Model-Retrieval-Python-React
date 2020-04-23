import re
import unittest

class stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return self.stack == []

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def get_stack(self):
        return self.stack

    def __len__(self):
        return len(self.stack)


def infix_to_postfix(query):
    list_operator = ['(', ')', 'or', 'and', 'not']
    priority_operator = [0, 0, 1, 2, 3]
    operator_stack = stack()
    postfix = stack()
    precedence = {}
    for i in range(len(list_operator)):
        precedence[list_operator[i]] = priority_operator[i]

    list_token = re.findall(r"([a-zA-Z]+|\(|\))", query)
    for token in list_token:
        if token not in precedence:
            postfix.push(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            head = operator_stack.pop()
            while head != '(':
                postfix.push(head)
                head = operator_stack.pop()
        else:
            while operator_stack.__len__() > 0 and (precedence[operator_stack.peek()] >= precedence[token]):
                postfix.push(operator_stack.pop())
            operator_stack.push(token)

    while operator_stack.__len__() > 0:
        postfix.push(operator_stack.pop())
    return postfix.get_stack()

class TestInfixToPostfix(unittest.TestCase):

    def setUp(self):
        self.expected = ['gatal', 'perih', 'merah', 'or', 'not', 'and']
        self.result = infix_to_postfix('gatal and not (perih or merah)')

    def test_query(self):
        self.assertCountEqual(self.result, self.expected, "Should be ['gatal', 'perih', 'merah', 'or', 'not', 'and']")


if __name__ == '__main__':
    unittest.main()
