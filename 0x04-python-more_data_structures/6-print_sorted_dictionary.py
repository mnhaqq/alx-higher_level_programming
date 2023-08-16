#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    arr = []
    for key, value in a_dictionary.items():
        arr.append([key, value])
    arr.sort()
    new_dict = dict()
    for pair in arr:
        new_dict[pair[0]] = pair[1]
    for key, value in new_dict.items():
        print(f"{key}: {value}")
