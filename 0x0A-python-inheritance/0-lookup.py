#!/usr/bin/python3
"""
Module containing a function returning available attributes
and methods of an object
"""


def lookup(obj):
    """
    Function that returns list of attributes and objects of
    an object

    Args:
        obj: object
    """
    return dir(obj)
