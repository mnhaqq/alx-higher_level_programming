#!/usr/bin/python3
"""
Module containing one function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file

    Args:
        filename: name of file to write the text to
        text: text to write to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
