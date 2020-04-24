from typing import Iterable


class Stack:
    def __init__(self, *args: Iterable[Iterable]):
        temp = []
        for arg in args:
            temp += arg
        self.stack = list(temp)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError

    def get(self):
        return self.stack

    def size(self):
        return len(self)

    def __len__(self):
        return len(self.stack)
