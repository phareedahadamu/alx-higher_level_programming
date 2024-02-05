#!/usr/bin/python3
""" A function that returns True if the object
is exactly an instance of the specified class;
otherwise False"""


def is_same_class(obj, a_class):
    """ obj: The object to be checked
        a_class: The class"""

    return (True if type(obj) is a_class else False)
