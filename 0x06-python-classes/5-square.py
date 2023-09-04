#!/usr/bin/python3
"""Defines a square"""


class Square:
    """A square

    Defines a square with optional parameter size
    """
    def __init__(self, size=0):
        self.__size = size

    """Area of square

    Computes the area of a square give length of a side
    """
    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        "Gets size of square"
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Print square

    Prints a square of size __size
    """
    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
