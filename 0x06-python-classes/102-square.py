#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Instantiation"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        return (self.size == other.size)

    def __ne__(self, other):
        return (self.size != other.size)

    def __lt__(self, other):
        return (self.size < other.size)

    def __le__(self, other):
        return (self.size <= other.size)

    def __gt__(self, other):
        return (self.size > other.size)

    def __ge__(self, other):
        return (self.size >= other.size)
