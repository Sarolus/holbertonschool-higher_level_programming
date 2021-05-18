#!/usr/bin/python3

"""
Square class

This class defines an square, initialize it's size, set it
using given value and give it's area.

"""


class Square():
    """
    Square Class

    Attributes:
        __size (int): Size of a square
    """
    __size = 0

    def __init__(self, prmSize=0):
        """
        __init__ method
        Args:
            prmSize (int): size of a square
        """
        self.size = prmSize

    def area(self):
        """
        area method

        Returns the area of a square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        size method

        Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, prmValue):
        """
        size method
        Args:
            prmValue (int): Value of a size of a square
        """
        self.__size = prmValue
        if not isinstance(prmValue, int):
            raise TypeError("size must be an integer")
        if prmValue < 0:
            raise ValueError("size must be >= 0")
