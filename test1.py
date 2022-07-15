from itertools import count
from multiprocessing.sharedctypes import Array
from unittest import TestCase, main
from notarray import zero


class ZeroTestCase(TestCase):
    def test_1_case(self):
        self.assertTrue(zero(n=[0, 1, 0, 3, 12]))
    
    def test_2_case(self):
        self.assertTrue(zero(n=[1, 7, 0, 0, 8, 0, 10, 12, 0, 4]))