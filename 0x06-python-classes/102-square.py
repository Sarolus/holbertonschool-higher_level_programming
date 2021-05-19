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

    def __eq__(self, object):
        """
        Equal method

        Make comparison using == operator possible.

        Args:
            object: object to compare.
        """
        if isinstance(object, Square):
            return self.area() == object.area()

    def __lt__(self, object):
        """
        Lower method

        Make comparison using < operator possible.

        rgs:
            object: object to compare.
        """
        if isinstance(object, Square):
            return self.area() < object.area()

    def __gt__(self, object):
        """
        Upper method

        Make comparison using > operator possible.

        rgs:
            object: object to compare.
        """
        if isinstance(object, Square):
            return self.area() > object.area()

    def __le__(self, object):
        """
        Equal or lower method

        Make comparison using <= operator possible.

        rgs:
            object: object to compare.
        """
        if isinstance(object, Square):
            return self.area() <= object.area()

    def __ge__(self, object):
        """
        Equal or Upper method

        Make comparison using >= operator possible.

        rgs:
            object: object to compare.
        """
        if isinstance(object, Square):
            return self.area() >= object.area()

    def __ne__(self, object):
        """
        Inequal method

        Make comparison using != operator possible.

        rgs:
            object: object to compare.
        """
        if isinstance(object, Square):
            return self.area() != object.area()
