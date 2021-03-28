"""Some of those clasic data structure you know and love."""

from typing import Any


class Stack:
    def __init__(self, *args) -> None:
        self.stack = list()
        for item in args:
            self.stack.append(item)

    def raise_if_empty(func):
        def wrapper_func(self, *args, **kwargs):
            if not self.stack:
                raise Exception("Empty stack exception.")
            x = func(self, *args, **kwargs)
            return x

        return wrapper_func

    def push(self, item) -> None:
        self.stack.append(item)

    @raise_if_empty
    def pop(self) -> Any:
        buffer = self.stack[-1]
        del self.stack[-1]
        return buffer

    @raise_if_empty
    def peek(self) -> Any:
        return self.stack[-1]

    def index_of(self, target) -> int:
        """Returns the distance between the top of the stack and the nearest instance of the target to the top."""
        for i, item in enumerate(reversed(self.stack)):
            if item == target:
                return i
        raise Exception(
            "Target not in stack"
        )  # ? Should this return -1 instead of raising?

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


class Queue:
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
        del self.queue[0]
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


class LLNode:
    def __init__(self, item) -> None:
        self.next = None
        self.data = item

    def is_tail(self) -> bool:
        return self.next == None

    def __repr__(self) -> str:
        return f"<Linked List Node Object {hex(id(self))}>"

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    # Head
    # ? Tail

    def __init__(self, *args) -> None:
        self.head = None
        for item in args:
            self.append(item)

    def scan(self) -> Any:
        if self.head == None:
            return None
        buffer = self.head
        yield buffer
        if not buffer.is_tail():
            buffer = buffer.next

    def append(self, item) -> None:
        if self.head == None:
            self.head = LLNode(item)
            return None
        buffer = self.head
        while not buffer.is_tail():
            buffer = buffer.next
        buffer.next = LLNode(item)

    def prepend(self, item) -> None:
        new_head = LLNode(item)
        new_head.next = self.head
        self.head = new_head

    def insert_after(self, item, target) -> None:
        pass

    def remove(self, item) -> None:
        pass

    def is_cyclical(self) -> bool:
        pass

    def index_of(self, target) -> int:
        pass

    def __len__(self) -> int:
        l = 0
        if self.head == None:
            return l
        for i in self.scan():
            l += 1
        return l

    def __bool__(self) -> bool:
        return self.head != None

    def __contains__(self, target) -> bool:
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print(s.index_of(3))