#!/usr/bin/python3
"""This defines a locked class"""


class LockedClass:
    """allows only one new instance attribute"""

    __slots__ = ["first_name"]
