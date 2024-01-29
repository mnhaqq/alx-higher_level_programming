#!/usr/bin/python3
"""Defines a rectangle subclass of the base geometry class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle"""

    def __init__(self, width, height):
        """
        Initializes a rectangle object

        Args:
            width: width of the rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
