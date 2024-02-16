#!/usr/bin/python3
""" Defines a class Base"""
import json


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
        """returns the JSON string representation of list_dictionaries"""
        return "[]" if (list_dictionaries is None or len(list_dictionaries)
                        == 0) else json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = []
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                f.write(Base.to_json_string(list_dicts))
