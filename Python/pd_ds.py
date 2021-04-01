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
        self.current = None
        for item in args:
            self.append(item)

    def _prepend_node(self, node: LLNode) -> None:
        node.next = self.head
        self.head = node

    def prepend(self, item: Any) -> None:
        new_node = LLNode(item)
        self._prepend_node(new_node)

    def scan(self) -> LLNode:
        if self.head is None:
            return
        buffer = self.head
        while not buffer.is_tail():
            yield buffer
            buffer = buffer.next
        yield buffer

    def find_tail(self) -> LLNode:
        for node in self.scan():
            if node.is_tail():
                return node

    def _append_node(self, node: LLNode) -> None:
        if self.head is None:
            self.head = node
        self.find_tail().next = node

    def append(self, item) -> None:
        new_node = LLNode(item)
        self._append_node(new_node)

    def insert_after(self, item, target) -> None:
        for node in self.scan():
            if node.data == target:
                new_node = LLNode(item)
                new_node.next = node.next
                node.next = new_node

    def remove(self, target) -> None:
        if self.head and self.head.data == target:
            self.head = self.head.next
            return
        for node in self.scan():
            if node.next and node.next.data == target:
                node.next = node.next.next
                return
        raise ValueError(f"{target} not in LinkedList.")

    def is_cyclical(self) -> bool:
        pass

    def index_of(self, target) -> int:
        pass

    def __len__(self) -> int:
        if self.head is None:
            return 0
        n = 0
        for i in self.scan():
            n += 1
        return n

    def __bool__(self) -> bool:
        return self.head != None

    def __contains__(self, target) -> bool:
        for n in self.scan():
            if n.data == target:
                return True
        return False

    def __repr__(self) -> str:
        return f"<Linked List {hex(id(self))}>"

    def __str__(self) -> str:
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.current = self.head
        print(f"Current = {self.current}")
        if self.current is not None:
            buffer = self.current
            self.current = self.current.next
            print(f"New Current = {self.current}")
            return buffer
        else:
            raise StopIteration

    def __getitem__(self, target: int) -> LLNode:
        for i, node in enumerate(self.scan()):
            if i == target:
                return node
        raise IndexError("LinkedList Index out of range")


if __name__ == "__main__":
    l = LinkedList()

    for n in l.scan():
        print("UH OH")

    l.prepend(0)
    l.prepend(18)
    l.prepend(9)

    l.append(44)
    l.append(55)

    for n in l.scan():
        print(n)