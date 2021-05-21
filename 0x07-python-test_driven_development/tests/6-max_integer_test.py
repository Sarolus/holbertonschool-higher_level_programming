#!/usr/bin/python3

"""
Unittest for task 6 max_integer.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """
        Test when no list is passed or when empty
        list is passed.
        """
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))

    def test_equal_values(self):
        """
        Test when all the values are the same
        """
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_unique_value(self):
        """
        Test when only one value is given
        """
        self.assertEqual(max_integer([2]), 2)

    def test_right_output(self):
        """
        Test when given an appropriate list
        """
        self.assertEqual(max_integer([25, 12, 9, 13]), 25)

    def test_negative_values(self):
        """
        Test when given all negative values
        """
        self.assertEqual(max_integer([-98, -54, -2 ,-33]), -2)

    def test_float_values(self):
        """
        Test when given all values in float
        """
        self.assertEqual(max_integer([1.2, 4.8, 9.2, 7.2]), 9.2)

    def test_insert_string(self):
        """
        Test when one value is a string
        """
        with self.assertRaises(TypeError):
            max_integer([2, "C is fun", 3, 9])
    