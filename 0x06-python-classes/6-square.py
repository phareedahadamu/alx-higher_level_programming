#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Instantiation"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not
                all(isinstance(num, int) for num in value) or not
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            [print() for i in range(0, self.__position[1])]
            i = 0
            while i < self.__size:
                k = 1
                while k <= self.__position[0]:
                    print(" ", end="")
                    k += 1
                j = 0
                while j < self.__size:
                    print("#", end="")
                    j += 1
                print()
                i += 1
