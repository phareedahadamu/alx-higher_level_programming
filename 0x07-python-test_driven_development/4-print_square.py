#!/usr/bin/python3
""" A function that prints a square with the character #"""


def print_square(size):
    """size is the size length of the square
    - size must be an integer else raise typeError
    - Size must be >= 0 else raise Value error
    - if size is a float and is less than 0, raise a TypeError exception
      with the message size must be an integer"""

    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
