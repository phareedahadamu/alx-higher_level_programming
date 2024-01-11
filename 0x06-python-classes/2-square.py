#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Instantiation"""
    def __init__(self, __size=0):
        try:
            if isinstance(__size, int) is False:
                raise TypeError
            if __size < 0:
                raise ValueError
            self.__size = __size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
