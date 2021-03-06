#!/usr/bin/python3

"""
Square module

This module defines an square, initialize it's size, set it
using given value and give it's area.

"""


class Square():
    """
    Square Class

    Attributes:
        __size (int): Size of a square
        __position (tuple): Position of a square
    """
    __size = 0
    __position = (0, 0)

    def __init__(self, prmSize=0, prmPosition=(0, 0)):
        """
        constructor method

        Args:
            prmSize (int): size of a square
            prmPosition (tuple): position of a square
        """
        self.size = prmSize
        self.position = prmPosition

    def __str__(self):
        """
        Convert to string in order to be print

        Returns a string containing all elements to
        print a square
        """
        string = ""
        if self.size is 0:
            string += "\n"
        else:
            for row in range(self.position[1]):
                string += "\n"
            for column in range(self.size):
                string += ' ' * self.position[0]
                string += '#' * self.size + "\n"
        return string[:-1]

    def area(self):
        """
        area method

        Returns the area of a square
        """
        return self.__size * self.__size

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

    @property
    def position(self):
        """
        position getter method

        Returns the position of a square
        """
        return self.__position

    @position.setter
    def position(self, prmValue):
        """
        position setter method

        Args:
            prmValue (tuple): Value of the position of a square
        """
        if isinstance(prmValue, tuple) and len(prmValue) == 2 and \
                isinstance(prmValue[0], int) and isinstance(prmValue[1], int) \
                and prmValue[0] >= 0 and prmValue[1] >= 0:
            self.__position = prmValue
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        my_print method

        Prints a square
        """
        if self.size == 0:
            print()
        else:
            for row in range(self.position[1]):
                print()
            for column in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
