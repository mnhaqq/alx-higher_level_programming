#!/usr/bin/python3
"""
Module containing rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates a rectangle object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x coordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets y coordinate of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints rectangle unto standard output"""
        for i in range(self.__y + self.__height):
            if i < self.__y:
                print()
                continue
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Prints rectangle details"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
                f"- {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Updates attributes of rectangle object"""
        attrs = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of a rectangle"""
        dic = dict()
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y

        return dic
