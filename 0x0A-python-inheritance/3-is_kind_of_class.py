#!/usr/bin/python3
"""
Module containing a function that checks if an object
is an instance of a specified class or if the object is an
instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Function that checks if an  object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class
    """
    return isinstance(obj, a_class)
