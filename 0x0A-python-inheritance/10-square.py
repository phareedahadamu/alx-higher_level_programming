#!/usr/bin/python3
""" Defines a class Square, that inherits from
Rectangle that inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Features of class square"""

    def __init__(self, size):
        """Instatiation of square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
