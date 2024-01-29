#!/usr/bin/python3
"""
Module containing a class that inherits from list class
"""


class MyList(list):
    """
    Class which inherits from list class
    """

    def print_sorted(self):
        """
        Function that prints a list sorted in ascending order
        """
        print(sorted(self))
