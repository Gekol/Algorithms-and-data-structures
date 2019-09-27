from unittest import TestCase
from ..counting_sort import work
from random import randint

class TestCountSort(TestCase):
    def testEmpty(self):
        self.assertEqual([], work([]))

    def testOneElem(self):
        self.assertEqual([1], work([1]))

    def testSameElem(self):
        data = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        res = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(res, work(data))

    def testSameElem(self):
        data = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        res = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(res, work(data))

    def testDifferent(self):
        data = [randint(0, 1000000) for i in range(1000)]
        res = sorted(data)
        self.assertEqual(res, work(data))

    def testSorted(self):
        data = [1, 2, 3, 5, 8, 10, 12, 13, 14, 15]
        self.assertEqual(data, work(data))

    def testAlmostSorted(self):
        data = [100, 3, 5, 8, 10, 13, 14, 17, 19, 20, 21, 32, 47, 54]
        self.assertEqual([3, 5, 8, 10, 13, 14, 17, 19, 20, 21, 32, 47, 54, 100], work(data))