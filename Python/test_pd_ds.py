import pytest
from pd_ds import Stack, Queue


class TestStack:
    def test_creation(self):
        s = Stack
        assert s is not None

    def test_empty_init(self):
        s = Stack()
        assert s.stack == []

    def test_one_init(self):
        s = Stack(1)
        assert s.stack == [1]

    def test_multiple_init(self):
        s = Stack(1, 2, 3)
        assert s.stack == [1, 2, 3]

    def test_push(self):
        s = Stack()
        s.push(1)
        assert s.stack == [1]

    def test_peek(self):
        s = Stack()
        s.push(1)
        assert s.peek() == 1
        s.push(2)
        assert s.peek() == 2

    def test_pop(self):
        s = Stack(1)
        assert s.pop() == 1
        s.push(2)
        s.push(3)
        assert s.pop() == 3
        assert s.pop() == 2

    def test_empty_peek(self):
        s = Stack()
        with pytest.raises(Exception):
            s.peek()

    def test_empty_pop(self):
        s = Stack()
        with pytest.raises(Exception):
            s.pop()

    def test_len(self):
        s = Stack()
        assert len(s) == 0
        s.push(1)
        assert len(s) == 1

    def test_index_of(self):
        s = Stack(1)
        assert s.index_of(1) == 0
        s.push(2)
        assert s.index_of(1) == 1
        s.push(1)
        assert s.index_of(1) == 0

    def test_missing_index_of(self):
        s = Stack()
        with pytest.raises(Exception):
            s.index_of(1)

    def test_contains(self):
        s = Stack()
        assert 1 not in s
        s.push(2)
        assert 2 in s


class TestQueue:
    def test_creation(self):
        q = Queue()
        assert q is not False

    def test_empty_init(self):
        q = Queue()
        assert q.queue == []

    def test_one_init(self):
        q = Queue(1)
        assert q.queue == [1]

    def test_multiple_init(self):
        q = Queue(1, 2, 3)
        assert q.queue == [1, 2, 3]

    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        assert q.queue == [1]
        q.enqueue(2)
        assert q.queue == [1, 2]

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        assert q.dequeue() == 2

    def test_peek(self):
        q = Queue(1)
        q_buffer = q.queue
        assert q.peek() == 1
        assert q.queue == q_buffer

    def test_empty_dequeue(self):
        q = Queue()
        with pytest.raises(Exception):
            q.dequeue()

    def test_empty_peek(self):
        q = Queue()
        with pytest.raises(Exception):
            q.peek()

    def test_len(self):
        q = Queue()
        assert len(q) == 0
        q.enqueue(1)
        assert len(q) == 1
        q.enqueue(2)
        assert len(q) == 2
        q.dequeue()
        assert len(q) == 1

    def test_index_of(self):
        q = Queue(1)
        assert q.index_of(1) == 0
        q.enqueue(2)
        assert q.index_of(2) == 1
        q.dequeue()
        assert q.index_of(2) == 0

    def test_missing_index_of(self):
        q = Queue()
        with pytest.raises(Exception):
            q.index_of(1)

    def test_contains(self):
        q = Queue(1)
        assert 1 in q
        assert 2 not in q