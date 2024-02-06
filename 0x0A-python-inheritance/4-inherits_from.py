#!/usr/bin/python3
"""Defines inherits_from"""


def inherits_from(obj, a_class):
    """ A function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) froom the specified class;
    otherwise False"""

    subclasses = a_class.__subclasses__()
    for i in subclasses:
        if isinstance(obj, i):
            return True
    return False
