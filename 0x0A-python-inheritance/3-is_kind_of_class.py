#!/usr/bin/python3
"""Defines is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object is an instance of, or if
    the object is an instance of a class that inherited from, the specified
    class; otherwise False."""
    return (True if isinstance(obj, a_class) else False)
