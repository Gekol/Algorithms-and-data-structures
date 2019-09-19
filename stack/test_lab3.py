from unittest import TestCase
from lab3 import Stack

class TestStack(TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(4)
        stack.push(3)
        self.assertEqual([1, 2, 4, 3], stack.stack)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        res = stack.pop()
        self.assertEqual(1, res)

    def test_peek(self):
        stack = Stack()
        res = stack.peek()
        self.assertEqual("Stack is empty!!!", res)

    def test_change_position(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.change_last_first()
        self.assertEqual([3, 2, 1], stack.stack)

    def test_reverse(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(5)
        stack.push(4)
        stack.push(3)
        stack.reverse()
        self.assertEqual([3, 4, 5, 2, 1], stack.stack)

    def test_check_True(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(5)
        stack.push(4)
        stack.push(3)
        res = stack.check(5)
        self.assertEqual(True, res)

    def test_check_False(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(5)
        stack.push(4)
        stack.push(3)
        res = stack.check(0)
        self.assertEqual(False, res)

    def test_clear(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(5)
        stack.push(4)
        stack.push(3)
        stack.clear()
        self.assertEqual([], stack.stack)