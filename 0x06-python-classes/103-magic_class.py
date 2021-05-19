#!/usr/bin/python3

"""
Magic class Task 10

This class was retrieved from Bytecodes for the task 10 of project
0x06-python-classes.
"""

import math


class MagicClass:
    """
    This class defines a circle of radius self.__radius
    """

    def __init__(self, radius=0):
        """
        constructor method

        Args:
            radius (int): radius of a circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        area method

        Returns the area of a circle
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        circumference method

        Returns the cirumference of a circle
        """
        return 2 * math.pi * self.__radius
