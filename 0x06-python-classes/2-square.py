#!/usr/bin/python3

"""
Square class

This class defines an square and initialize it's size.

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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
