from unittest import TestCase
from lab4 import Queue

class TestQueue(TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(4)
        queue.enqueue(3)
        self.assertEqual([1, 2, 4, 3], queue.queue)

    def test_pop(self):
        queue = Queue()
        queue.enqueue(1)
        res = queue.dequeue()
        self.assertEqual(1, res)

    def test_peek(self):
        queue = Queue()
        res = queue.peek()
        self.assertEqual("Queue is empty!!!", res)

    def test_change_position(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.change_last_first()
        self.assertEqual([3, 2, 1], queue.queue)

    def test_reverse(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(5)
        queue.enqueue(4)
        queue.enqueue(3)
        queue.reverse()
        self.assertEqual([3, 4, 5, 2, 1], queue.queue)

    def test_check_True(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(5)
        queue.enqueue(4)
        queue.enqueue(3)
        res = queue.check(5)
        self.assertEqual(True, res)

    def test_check_False(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(5)
        queue.enqueue(4)
        queue.enqueue(3)
        res = queue.check(0)
        self.assertEqual(False, res)

    def test_clear(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(5)
        queue.enqueue(4)
        queue.enqueue(3)
        queue.clear()
        self.assertEqual([], queue.queue)