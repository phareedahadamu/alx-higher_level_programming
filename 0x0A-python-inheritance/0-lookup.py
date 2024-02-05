#!/usr/bin/python3

"""
- a function that returns the list of available attributes
and methods of an object
- Returns a list object
"""


def lookup(obj):
    """ obj : The object whose attributes are to be retrieved
        Returns a list of the attributes"""

    return (dir(obj))
