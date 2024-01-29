#!/usr/bin/python3
"""
Module containing one function for checking if an object is an
instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Function for checking if an object is an instance of a
    specified class

    Args:
        obj: object
        a_class: class
    """
    return type(obj) is a_class
