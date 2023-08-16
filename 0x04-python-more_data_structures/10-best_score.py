#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest_val = 0
    biggest_key = ""
    for key, value in a_dictionary.items():
        if value > biggest_val:
            biggest_val = value
            biggest_key = key
    return biggest_key
