#!/usr/bin/python3

"""
Rectangle module

This contains a rectangle class, it's area and
it's perimeter.
"""


class Rectangle():
    """Rectangle class"""
    __width = 0
    __height = 0
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        __init__ method
        Args:
            width (int): width of a rectangle
            height (int): height of a rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Return the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        __str__ printable method

        Returns an "informal" and printable string
        representation of the instance.
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            string += "\n"
        else:
            for char in range(self.__height):
                string += '#' * self.__width + "\n"

        return string[:-1]

    def __repr__(self):
        """
        __repr__ printable method

        Returns an "official" string representation
        of the instance
        """
        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"

    def __del__(str):
        """
        __del__ method

        Called when an instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
