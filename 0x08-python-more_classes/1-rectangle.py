#!/usr/bin/python3

"""
Rectangle module

This contains a rectangle class

"""


class Rectangle():
    """Rectangle class"""
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """
        __init__ method
        Args:
            width (int): width of a rectangle
            height (int): height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width property method

        Return the width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, prmValue):
        """
        width setter method

        Args:
            prmValue (int): value of width
        """
        if not isinstance(prmValue, int):
            raise TypeError("width must be an integer")
        if prmValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = prmValue

    @property
    def height(self):
        """
        height property method

        Return the height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, prmValue):
        """
        height setter method

        Args:
            prmValue (int): value of height
        """
        if not isinstance(prmValue, int):
            raise TypeError("height must be an integer")
        if prmValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = prmValue
