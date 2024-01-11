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

    def my_print(self):
        if self.size == 0:
            print()
        else:
            i = 0
            while i < self.__size:
                j = 0
                while j < self.__size:
                    print("#", end="")
                    j += 1
                print()
                i += 1
