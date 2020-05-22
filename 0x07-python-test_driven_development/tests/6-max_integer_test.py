#!/usr/bin/python3
"""Unittest max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests max_integer"""
    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

if __name__ == '__main__':
    unittest.main()
