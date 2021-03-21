"""Some of those clasic data structure you know and love."""

from typing import Any


class Stack():
    def __init__(self, *args) -> None:
        self.stack = list()
        for item in args:
            self.stack.append(item)

    def not_if_empty(func):
        def wrapper_func(self, *args, **kwargs):
            if not self.stack:
                raise Exception("Empty stack exception.")
            x = func(self, *args, **kwargs)
            return x
        return wrapper_func

    def push(self, item) -> None:
        self.stack.append(item)

    @not_if_empty
    def pop(self) -> Any:
        buffer = self.stack[-1]
        del(self.stack[-1])
        return buffer

    @not_if_empty
    def peek(self) -> Any:
        return self.stack[-1]

    def index_of(self, target) -> int:
        for i, item in enumerate(self.stack):
            if item == target:
                return len(self) - i - 1
        raise Exception("Target not in stack")

    def __len__(self) -> int:
        return len(self.stack)

    def __contains__(self, target) -> bool:
        for item in self.stack:
            if item == target:
                return True
        return False

    def __repr__(self) -> str:
        return f"<Stack object {hex(id(self))}>"

    def __str__(self) -> str:
        return str(self.stack)


class Queue():
    def __init__(self, *args) -> None:
        self.queue = list()
        for item in args:
            self.queue.append(item)

    def not_if_empty(func):
        def wrapper_func(self, *args, **kwargs):
            if not self.queue:
                raise Exception("Empty stack exception.")
            x = func(self, *args, **kwargs)
            return x
        return wrapper_func

    def enqueue(self, item) -> None:
        self.queue.append(item)

    @not_if_empty
    def dequeue(self) -> Any:
        buffer = self.queue[0]
        del(self.queue[0])
        return buffer

    @not_if_empty
    def peek(self) -> Any:
        return self.queue[0]

    def index_of(self, target) -> int:
        for i, item in enumerate(self.queue):
            if item == target:
                return i
        raise Exception("Target not in queue.")

    def __len__(self) -> int:
        return len(self.queue)

    def __contains__(self, target) -> bool:
        for item in self.queue:
            if item == target:
                return True
        return False

    def __repr__(self) -> str:
        return f"Queue object {hex(id(self))}"

    def __str__(self) -> str:
        return str(self.queue)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print(s.index_of(3))