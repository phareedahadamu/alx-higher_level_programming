#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        #positive integers
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        #with float
        self.assertAlmostEqual(max_integer([1, 3.3, 0.99, -10]), 3.3)
        #with all negative integers
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4]), -1)
        #with duplicate integers
        self.assertAlmostEqual(max_integer([1, 4, 3, 4]), 4)
        #with empty list
        self.assertAlmostEqual(max_integer(), None)

    def test_errors(self):
        #int passed as arg instead of list
        self.assertRaises(TypeError, max_integer, 22)
        #string included in the list
        self.assertRaises(TypeError, max_integer, [1, 2, 'Hi', 3])
        #set passed instead of list
        self.assertRaises(TypeError, max_integer, {1, 2, 3, 4})
