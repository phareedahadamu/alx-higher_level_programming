#!/usr/bin/python3
""" Defines a class Rectangle"""


class Rectangle:
    """ Instantiation, property getter and setter of width,
        property getter and setter of height, area method,
        perimeter method, __str__ method to define the
        string representation, __repr__ method to define the
        string representation that can be used to create an instance by
        using eval()"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (0 if (self.__width == 0 or self.__height == 0)
                else (2 * (self.__width + self.__height)))

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ('')
        for i in range(0, self.__height):
            [print("#", end="") for j in range(0, self.__width)]
            if i < self.height - 1:
                print()
        return ('')

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
