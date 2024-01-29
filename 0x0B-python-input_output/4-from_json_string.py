#!/usr/bin/python3
"""
Module containing one function that returns python object from JSON string
"""
import json


def from_json_string(my_str):
    """
    Function that returns python object from JSON string

    Args:
        my_str: JSON string
    """
    return json.loads(my_str)
