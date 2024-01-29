#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dic = a_dictionary.copy()
    for key, val in dic.items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary
