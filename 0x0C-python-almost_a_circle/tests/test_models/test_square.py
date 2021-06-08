#!/usr/bin/python3

"""
    Module containing tests for the Square Class.
"""
import unittest
from models.square import Square


class Square_tests(unittest.TestCase):
    """
        Tests Cases for the Square Class
    """

    def test_parameters_init(self):
        """
            Test initialization of the Square
            class.
        """
        self.square = Square(5, 2, 2)

        """Test width initialization"""
        self.assertEqual(5, self.square.width)

        """Test height initialization"""
        self.assertEqual(5, self.square.height)

        """Test x initialization"""
        self.assertEqual(2, self.square.x)

        """Test y initialization"""
        self.assertEqual(2, self.square.y)
