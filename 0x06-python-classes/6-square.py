#!/usr/bin/python3
"""Defines a square"""


class Square:
    """A square

    Defines a square with optional parameter size
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        "Gets position of square"
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    """Print square

    Prints a square of size __size
    """
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1] + self.__size):
            if i < self.__position[1]:
                print()
                continue
            for j in range(self.__position[0] + self.__size):
                if j < self.__position[0]:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()
