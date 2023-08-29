#!/usr/bin/python3
"""Defines a square"""


class Square:
    """A square

    Defines a square with optional parameter size
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Area of square

    Computes the area of a square give length of a side
    """
    def area(self):
        return self.__size ** 2
