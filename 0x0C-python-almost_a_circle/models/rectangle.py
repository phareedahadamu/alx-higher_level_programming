#!/usr/bin/python3
""" Defines the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ Features of Rectangle class that inherits
    from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not (isinstance(value, int)):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not (isinstance(value, int)):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Defines the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """ prints to stdout the rectangle represented by #"""
        for i in range(0, self.__height):
            [print("#", end='') for j in range(0, self.__width)]
            print()

    def __str__(self):
        """ The string representation of Rectangle when it is printed"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))
