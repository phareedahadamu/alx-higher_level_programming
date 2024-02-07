#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Features of BaseGeometry"""

    def area(self):
        """Defines the base geometry's area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ - Validates value
        - name is always a string
        - if value is not an integer: raise a TypeError exception
        - if value is less or equal to 0: raise a ValueError exception"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


""" Defines a class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """ Features of Rectangle"""

    def __init__(self, width, height):
        """Instantiation of rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
