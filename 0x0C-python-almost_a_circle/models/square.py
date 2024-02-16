#!/usr/bin/python3
""" Defines the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Features of class Square
    Inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation of Square when printed"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
