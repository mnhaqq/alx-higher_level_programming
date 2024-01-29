#!/usr/bin/python3
"""
Module containing one function that appends a string to the
end of a text file
"""


def append_write(filename="", text=""):
    """
    Function that appends string to end of a text file

    Args:
        filename: name of file
        text: text to append to file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
