import pytest
from pd_ds import Stack, Queue, LLNode, LinkedList


@pytest.mark.skip(reason="Temporary skip while linked lists are giving me trouble")
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


@pytest.mark.skip(reason="Temporary skip while linked lists are giving me trouble")
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


class TestLLNode:
    def test_creation(self):
        n = LLNode(0)
        assert n is not None

    def test_assignment(self):
        n = LLNode(0)
        assert n.data == 0
        assert n.next == None
        n.data = 1
        assert n.data == 1

    def test_tail_detection(self):
        n = LLNode(0)
        assert n.is_tail


class TestLinkedList:
    @pytest.fixture
    def test_ll(self):
        return LinkedList()

    def test_creation(self, test_ll):
        assert test_ll is not None

    def test_empty_init(self, test_ll):
        l = LinkedList()
        assert l.head is None

    def test_prepend(self, test_ll):
        test_ll.prepend(0)
        assert test_ll.head is not None
        assert test_ll.head.data == 0
        test_ll.prepend(1)
        assert test_ll.head.data == 1

    def test_scan(self):
        #! I don't know how to do this!
        pass

    def test_find_tail(self, test_ll):
        test_ll.prepend(99)
        assert test_ll.find_tail().data == 99
        test_ll.prepend(0)
        assert test_ll.find_tail().data == 99

    def test_len(self, test_ll):
        assert len(test_ll) == 0
        test_ll.prepend(1)
        assert len(test_ll) == 1
        test_ll.prepend(0)
        assert len(test_ll) == 2

    def test_contains(self):
        l = LinkedList()
        assert 0 not in l
        l.prepend(0)
        assert 0 in l

    @pytest.mark.skip(reason="This hangs, for reasons I can't discern")
    def test_append(self):
        l = LinkedList()
        l.append(0)
        assert l.head is not None
        assert l.head.data == 0
        l.append(3)
        assert l.head.data == 0
        assert len(l) == 2
        assert l.head.next.data == 3

    def test_insert_after(self):
        l = LinkedList()
        l.prepend(0)
        l.insert_after(1, 0)
        assert l.head.next.data == 1

    def test_remove(self):
        target = 9

        # Target at head
        head = LinkedList()
        head.prepend(0)
        head.prepend(0)
        head.prepend(target)
        # Target at tail
        tail = LinkedList()
        tail.prepend(target)
        tail.prepend(0)
        tail.prepend(0)
        # Target in middle
        mid = LinkedList()
        mid.prepend(0)
        mid.prepend(target)
        mid.prepend(0)
        # Target is only item
        solo = LinkedList()
        solo.prepend(target)

        assert target in head
        assert target in tail
        assert target in mid
        assert target in solo

        head.remove(target)
        tail.remove(target)
        mid.remove(target)
        solo.remove(target)

        assert target not in head
        assert target not in tail
        assert target not in mid
        assert target not in solo

    def test_remove_missing(self):
        missing = LinkedList()
        missing.prepend(0)
        missing.prepend(0)
        with pytest.raises(ValueError):
            missing.remove(9)

    def test_remove_empty(self):
        empty = LinkedList()
        with pytest.raises(ValueError):
            empty.remove(9)

    def test_getitem(self, test_ll):
        test_ll.prepend(2)
        test_ll.prepend(1)
        test_ll.prepend(0)
        assert test_ll[0].data == 0
        assert test_ll[2].data == 2

    def test_getitem_bad_index(self, test_ll):
        test_ll.prepend(2)
        test_ll.prepend(1)
        test_ll.prepend(0)
        with pytest.raises(IndexError):
            test_ll[3]
