#!/usr/bin/python3
""" Defines the function def add_integer(a, b=98):
- A function that adds 2 integers
- a and b must be integers or floats, otherwise raise a TypeError\
        exception with the message a must be an integer or b must be an integer
- a and b must be first casted to integers if they are float
- Returns an integer: the addition of a and b"""


def add_integer(a, b=98):
    """ The function documentation
    Accepts 2 args a and b
    b is initialised to 98"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if (isinstance(a, float)) is True:
        a = int(a)
    if (isinstance(b, float)) is True:
        b = int(b)
    return a + b
