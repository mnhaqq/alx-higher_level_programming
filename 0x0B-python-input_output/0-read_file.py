#!/usr/bin/python3
"""
Module containing one function that reads a text file
and prints it to standard output
"""


def read_file(filename=""):
    """
    Function that reads a text file and prints it to standard output

    Args:
        filename: name of file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
