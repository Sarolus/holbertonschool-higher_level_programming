#!/usr/bin/python3

"""
    Module containing tests for the Base Class.
"""
import unittest
from models.base import Base


class Base_tests(unittest.TestCase):
    """
        Tests Cases for the Base Class
    """

    def test_id(self):
        """
            Test different uses of ID

            TestCases:
                # When no arguments are given 
                and that multiple times.
                # When a specific int argument
                is given.
                # When a negative int argument
                is given.
                # When a string argument is
                given.
        """
        b1 = Base()
        self.assertEqual(1, b1.id)

        b2 = Base()
        self.assertEqual(2, b2.id)

        b3 = Base()
        self.assertEqual(3, b3.id)

        b4 = Base(12)
        self.assertEqual(12, b4.id)

        b5 = Base()
        self.assertEqual(4, b5.id)

        b6 = Base(-4)
        self.assertEqual(-4, b6.id)

        b7 = Base()
        self.assertEqual(5, b7.id)

        b8 = Base("ID")
        self.assertEqual("ID", b8.id)
