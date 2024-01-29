#!/usr/bin/python3
"""
Module containing one function that writes an object to
a text file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file using JSON representation

    Args:
        my_obj: object
        filename: name of the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
