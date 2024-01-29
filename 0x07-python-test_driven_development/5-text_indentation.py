#!/usr/bin/python3
"""This module contains one function for printing text in specific format"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ptr = 0
    while ptr < len(text) and text[ptr] == " ":
        ptr += 1

    while ptr < len(text):
        print(text[ptr], end="")
        if text[ptr] == "\n" or text[ptr] in ".?:":
            if text[ptr] in ".?:":
                print("\n")
            ptr += 1
            while ptr < len(text) and text[ptr] == " ":
                ptr += 1
            continue
        ptr += 1
