from util import Stack
import re

def infix_to_postfix(query):
    operator_stack = Stack()
    postfix = Stack()
    precedence = {'(':0,')':0,'or':1,'and':2,'not':3}

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


