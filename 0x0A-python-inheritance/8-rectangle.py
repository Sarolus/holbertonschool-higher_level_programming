#!/usr/bin/python3

"""
    Module containing a rectangle class that
    inherits from the BaseGeometry class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        A rectangle class.
    """
    def __init__(self, width, height):
        """
            Initialization method.

            Args:
                width: width of a rectangle.
                height: height of a rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
