#!/usr/bin/python3
"""
Module containing class which describes student
"""


class Student:
    """
    Class describing student object
    """
    def __init__(self, first_name, last_name, age):
        """
        Function initializing student object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Function that retrieves dictionary representation of a Student object
        """
        return self.__dict__
