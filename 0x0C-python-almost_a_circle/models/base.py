#!/usr/bin/python3
""" Defines a class Base"""


class Base:
    """ Features of class Base:
        Private class attribute nb_objects
        __init__ method"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ """
        import json
        return "[]" if list_dictionaries is None or len(list_dictionaries) == 0 else json.dumps(list_dictionaries)


