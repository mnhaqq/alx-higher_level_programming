#!/usr/bin/python3
"""Module containing one function to print a square"""


def print_square(size):
    """
    Function to print a square

    Args:
        size: size of the square

    Raises:
        TypeError if size is not an integer
        ValueError if size is less than to zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for i in range(size):
        print("#" * size)
