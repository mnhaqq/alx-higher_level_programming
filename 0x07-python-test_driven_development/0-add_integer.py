#!/usr/bin/python3
"""
Module containg one function for adding 2 numbers
"""


def add_integer(a, b=98):
    """
    Function to add two numbers

    Args:
        a: first number
        b: second number

    Returns:
       Sum of the two integers

    Raises:
        TypeError if a or b is not an integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
