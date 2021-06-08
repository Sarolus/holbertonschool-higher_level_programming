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

    def test_update(self):
        """
            Test different uses of the update
            function of the rectangle instance.
        """
        """Test using simple arguments"""
        r1 = Rectangle(32, 4, 2, 16, 8)
        r1.update(64, 8, 4, 32, 16)
        self.assertEqual(64, r1.id)
        self.assertEqual(8, r1.width)
        self.assertEqual(4, r1.height)
        self.assertEqual(32, r1.x)
        self.assertEqual(16, r1.y)

        """Test using key and value arguments"""
        r2 = Rectangle(32, 4, 2, 16, 8)
        r2.update(id=64, width=8, height=4, x=32, y=16)
        self.assertEqual(64, r2.id)
        self.assertEqual(8, r2.width)
        self.assertEqual(4, r2.height)
        self.assertEqual(32, r2.x)
        self.assertEqual(16, r2.y)
