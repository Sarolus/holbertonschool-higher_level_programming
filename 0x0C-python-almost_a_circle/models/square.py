#!/usr/bin/python3

"""
    Square Class Module
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square Class
    """
    __size = None
    __x = None
    __y = None

    def __init__(self, size, x=0, y=0, id=None):
        """
            Constructor Method
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Getter Method of Size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Setter Method of Size
        """
        self.attribute_validator("size", value)
        self.__size = value

    def __str__(self):
        """
            Set a string representation of a
            square values.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x,
                                                 self.__y, self.__size)
