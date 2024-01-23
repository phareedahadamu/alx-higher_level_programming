#!/usr/bin/python3
""" Defines a class Rectangle"""


class Rectangle:
    """ Instantiation, property getter and setter of width,
        property getter and setter of height, area method,
        perimeter method, __str__ method to define the
        string representation, __repr__ method to define the
        string representation that can be used to create an instance by
        using eval(), __del__ method defines what happens when an instance
        is deleted"""
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_2 if (rect_2.width * rect_2.height > rect_1.width
                * rect_1.height) else rect_1)

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (0 if (self.__width == 0 or self.__height == 0)
                else (2 * (self.__width + self.__height)))

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ('')
        for i in range(0, self.__height):
            [print("{}".format(self.print_symbol),
             end="") for j in range(0, self.__width)]
            if i < self.height - 1:
                print()
        return ('')

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
