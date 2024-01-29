#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """This class represents a base geometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value

        Args:
            name(str): name
            value(int): value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
