#!/usr/bin/python3
""" Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Features of Rectangle"""

    def __init__(self, width, height):
        """Instantiation of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the rectangles area"""
        return (self.__width * self.__height)

    def __str__(self):
        """String representation of the rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
