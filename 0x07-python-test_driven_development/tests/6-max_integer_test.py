#!/usr/bin/python3
"""Unittest max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests max_integer"""
    def test_EmptyList(self):
        self.assertEqual(max_integer([]), None)
    def test_Normal(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_negativeNumbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    def testnegativeAndpositive(self):
        self.assertEqual(max_integer([-4, 3, -2, 1]), 3)
    def test_decimals(self):
        self.assertEqual(max_integer([2, 4.7, 1, 1.2]), 4.7)
    def test_errorParameter(self):
        with self.assertRaises(TypeError):
            max_integer([3, '2', 1])
    def test_errorParamterList(self):
        with self.assertRaises(TypeError):
            max_integer([3, [2], 1])
    def test_parameters(self):
        with self.assertRaises(TypeError):
            max_integer(1)
            
if __name__ == '__main__':
    unittest.main()
