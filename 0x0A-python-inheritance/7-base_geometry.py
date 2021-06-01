#!/usr/bin/python3

"""
    Module containing a geometry class.
"""


class BaseGeometry():
    """
        A class containing some geometry functions.
    """
    def area(self):
        """
            Method that calculate the area of a geometric
            structure (square, rectangle, etc...). Not
            implemented yet.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Method that validates (or not) the given value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
