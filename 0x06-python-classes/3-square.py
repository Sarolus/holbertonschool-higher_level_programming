#!/usr/bin/python3

"""
Square class

This class defines an square, initialize it's size and
give it's area.

"""


class Square():
    """Square Class"""
    def __init__(self, size=0):
        """
        __init__ method
        Args:
            size (int): size of a square
        Raises:
            TypeError: Error if size is not an int.
            ValueError: Error if size is less than 0.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        area method

        Returns the area of a square
        """
        return self.__size * self.__size
