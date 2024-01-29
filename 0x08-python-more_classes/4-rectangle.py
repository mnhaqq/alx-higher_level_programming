#!/usr/bin/python3
"""
This module defines a rectangle
"""


class Rectangle:
    """
    Documentation for rectangle

    This class defines a rectange
    """

    def __init__(self, width=0, height=0):
        """
        Initializes rectangle class

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        output = ""
        if self.__width == 0 or self.__height == 0:
            return output

        for i in range(self.__height):
            for j in range(self.__width):
                output += "#"
            if i == self.__height - 1:
                break
            output += "\n"
        return output

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    @property
    def width(self):
        """Gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
