from typing import Iterable

class stack:
    def __init__(self, *args: Iterable[Iterable]):
        temp = []
        for arg in args:
            temp+=arg
        self.stack = list(temp)
    def push(self, data):
        self.stack.append(data)

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
