#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            new_str += chr(ord(c) - 32)
        else:
            new_str += c
    print("{:s}".format(new_str))
