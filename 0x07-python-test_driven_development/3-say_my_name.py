#!/usr/bin/python3
"""Module containing one function that prints a person's name"""


def say_my_name(first_name, last_name=""):
    """
    Function to print a person's name

    Args:
        first_name: person's first name
        last_name: person's last name

    Raises:
        TypeError: If either the first_name and last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
