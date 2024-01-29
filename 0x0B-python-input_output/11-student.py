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

    def to_json(self, attrs=None):
        """
        Function that retrieves dictionary representation of a Student object
        """
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if type(attr) is not str:
                return self.__dict__
        dic = dict()
        for attr in attrs:
            if attr in self.__dict__:
                dic[attr] = self.__dict__.get(attr)
        return dic

    def reload_from_json(self, json):
        """
        Function that replaces all attributes of student instance
        """
        if not json:
            return
        self.__dict__ = dict()
        for key in json.keys():
            self.__dict__[key] = json[key]
