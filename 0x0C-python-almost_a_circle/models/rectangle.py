#!/usr/bin/python3

"""
    Rectangle Class Module
"""
from models.base import Base


class Rectangle(Base):
    """
        Rectangle Class
    """
    __width = None
    __height = None
    __x = None
    __y = None

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Constructor Method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Getter Method of Width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter Method of Width
        """
        self.attribute_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
            Getter Method of Height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter Method of Height
        """
        self.attribute_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
            Getter Method of X
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Setter Method of X
        """
        self.attribute_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """
            Getter Method of Y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Setter Method of Y
        """
        self.attribute_validator("y", value)
        self.__y = value

    def attribute_validator(self, name, value):
        """
            Method that validates (or not) the given value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
            Calculate the area of the rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
            Prints in stdout the Rectangle instance using
            the character #.
        """
        print("\n" * self.__y, end="")
        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width, end="\n")

    def __str__(self):
        """
            Set a string representation of a
            rectangle values.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
            Assign an argument to each attribute
        """
        if args:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
