#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Instantiation"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
