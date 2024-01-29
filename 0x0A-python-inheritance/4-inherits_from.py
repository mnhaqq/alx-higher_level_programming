#!/usr/bin/python3
"""
Module containing function that checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Function that checks if an object is an instane of a subclass

    Args:
        obj: object
        a_class: specified class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
