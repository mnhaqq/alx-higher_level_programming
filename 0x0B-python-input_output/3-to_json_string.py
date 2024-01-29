#!/usr/bin/python3
"""
Module containing one function that returns JSON representation
of an object
"""
import json


def to_json_string(my_obj):
    """
    Function that returns JSON representation of an object

    Args:
        my_obj: object to parse to JSON
    """
    return json.dumps(my_obj)
