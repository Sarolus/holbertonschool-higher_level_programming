#!/usr/bin/python3

"""
    Module containing tests for the Rectangle Class.
"""
import unittest
from models.rectangle import Rectangle


class Rectangle_tests(unittest.TestCase):
    """
        Tests Cases for the Rectangle Class
    """

    def test_parameters_init(self):
        """
            Test initialization of the Rectangle
            class.
        """
        self.rectangle = Rectangle(8, 4, 32, 16, 64)

        """Test width initialization"""
        self.assertEqual(8, self.rectangle.width)

        """Test height initialization"""
        self.assertEqual(4, self.rectangle.height)

        """Test x initialization"""
        self.assertEqual(32, self.rectangle.x)

        """Test y initialization"""
        self.assertEqual(16, self.rectangle.y)

        """ Test ID initialization"""
        self.assertEqual(64, self.rectangle.id)

    def test_raised_errors(self):
        """
            Test error cases of the Rectangle
            class.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("Hello", 4, 32, 16, 64)
        with self.assertRaises(TypeError):
            r2 = Rectangle(8, "World", 32, 16, 64)
        with self.assertRaises(TypeError):
            r3 = Rectangle(8, 4, "Holberton", 16, 64)
        with self.assertRaises(TypeError):
            r3 = Rectangle(8, 4, 32, "School", 64)
        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 4, 32, 16, 64)
        with self.assertRaises(ValueError):
            r4 = Rectangle(8, 0, 32, 16, 64)
        with self.assertRaises(ValueError):
            r4 = Rectangle(8, 4, -32, 16, 64)
        with self.assertRaises(ValueError):
            r4 = Rectangle(-8, 4, 32, -16, 64)

    def test_area_uses(self):
        """
            Test cases of the use of the area
            calculating function.
        """
        r1 = Rectangle(8, 4)
        self.assertEqual(32, r1.area())

        r2 = Rectangle(2, 10)
        self.assertEqual(20, r2.area())

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r3.area())

        r4 = Rectangle(8, 4, 32, 16, 64)
        self.assertEqual(32, r4.area())

    def test_rectangle_displaying(self):
        """
            Test displaying different 
            rectangle instances.
        """
        
        """Dunno for know"""

    def test_rectangle_str_method(self):
        """
            Test printing rectangle values
            using the __str__ method
        """
        output = "[Rectangle] (64) 32/16 - 8/4"
        r1 = Rectangle(8, 4, 32, 16, 64)
        self.assertEqual(output, r1.__str__())
