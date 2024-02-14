#!/usr/bin/python3
""" Defines a class Student"""


class Student:
    """ Features of student"""

    def __init__(self, first_name, last_name, age):
        """ Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dict representation of Student"""
        obj_dict = self.__dict__
        my_dict = obj_dict.copy()
        if attrs is not None and (isinstance(attrs, list) and
                                  all(isinstance(item, str)
                                      for item in attrs)):
            for key in obj_dict:
                if key not in attrs:
                    my_dict.pop(key)
        return my_dict
