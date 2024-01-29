#!/usr/bin/python3
"""
Module containing a square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Reptesents a rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Creates a square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets size of square"""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes of square object"""
        attrs = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of a square"""
        dic = dict()
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic

    def __str__(self):
        """Prints square details"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
