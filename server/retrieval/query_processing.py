import re
from .boolean_model import BooleanModel
from .stack import Stack
from typing import List, Set, Tuple, Dict


def infix_to_postfix(query: str) -> List[str]:
    operator_stack: Stack = Stack()
    postfix: Stack = Stack()
    precedence: Dict[str, int] = {'(': 0, ')': 0, 'or': 1, 'and': 2, 'not': 3}

    list_token: List[str] = re.findall(r"([a-zA-Z]+|\(|\))", query)
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
    return postfix.get()


def postfix_evaluator(query: List[str], boolean_model: BooleanModel) -> Set[int]:
    temp_result: Stack = Stack()
    operator: Tuple[str] = ('or', 'and', 'not')
    for token_in_query in query:
        if token_in_query in operator:
            if token_in_query == 'not':
                temp_result.push(boolean_model.not_operator(temp_result.pop()))
            elif token_in_query == 'and':
                temp_result.push(temp_result.pop().intersection(temp_result.pop()))
            else:
                temp_result.push(temp_result.pop().union(temp_result.pop()))
        else:
            temp_result.push(boolean_model.get_indexes(token_in_query))

    if len(temp_result) > 1:
        raise ValueError

    return temp_result.pop()
