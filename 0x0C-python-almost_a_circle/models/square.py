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

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute"""
        if (args and len(args) != 0):
            i = 1
            for arg in args:
                if i == 1:
                    self.id = arg
                elif i == 2:
                    self.width = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'size':
                        self.width = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    elif key == 'id':
                        self.id = value

    def to_dictionary(self):
        """ returns the dict representation of Rectangle"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
