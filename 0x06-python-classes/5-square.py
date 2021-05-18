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
        constructor method

        Args:
            prmSize (int): size of a square
        """
        self.size = prmSize

    def area(self):
        """
        area method

        Returns the area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        size getter method

        Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, prmValue):
        """
        size setter method

        Args:
            prmValue (int): Value of a size of a square
        """
        self.__size = prmValue
        if not isinstance(prmValue, int):
            raise TypeError("size must be an integer")
        if prmValue < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """
        my_print method

        Prints a square
        """
        if self.size == 0:
            print('')
        for y in range(self.size):
            for x in range(self.size):
                print('#', end='')
            print('')
