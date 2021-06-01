#!/usr/bin/python3

"""
    Module containing a square class that
    inherits from the Rectangle class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        A square class
    """

    def __init__(self, size):
        """
            Initialization method.

            Args:
                size: size of a square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
            Calculate the area of a square.
        """
        return (self.__size ** 2)
