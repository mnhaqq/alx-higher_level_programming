#!/usr/bin/python3
"""
Module containing a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data structure
    for json serialization of an object

    Args:
        obj: instance of a class
    """
    return obj.__dict__
