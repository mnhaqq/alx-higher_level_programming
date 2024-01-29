#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEquals(max_integer([1, 2, 3, 4]), 4)
        self.assertEquals(max_integer([10, 12, 14, 17]), 17)
        self.assertEquals(max_integer([5]), 5)

    def test_unordered_list(self):
        self.assertEquals(max_integer([10, 9, 2, 7]), 10)
        self.assertEquals(max_integer([10, 20, 30, 20]), 30)

    def test_negatives(self):
        self.assertEquals(max_integer([10, -2, 2, 30]), 30)
        self.assertEquals(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        self.assertEquals(max_integer([]), None)
