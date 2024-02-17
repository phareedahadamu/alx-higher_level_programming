#!/usr/bin/python3
""" Defines a class Base"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        return [] if json_string is None else json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            subclass = cls(3, 5, 0, 0, 1)
        elif cls.__name__ == 'Square':
            subclass = cls(3, 0, 0, 1)
        Base.__nb_objects += 1
        subclass.update(**dictionary)
        return subclass

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            list_dict = Base.from_json_string(f.read())
        list_objs = []
        for i in list_dict:
            list_objs.append(cls.create(**i))
        return list_objs
