#!/usr/bin/python3
""" Defines a class Student"""


class Student:
    """ Features of student"""

    def __init__(self, first_name, last_name, age):
        """ Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dict representation of Student"""
        return self.__dict__
