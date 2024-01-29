#!/usr/bin/python3
"""
Module containing script for add in arguments to a list and saving them
"""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    arr = []
    for i in range(1, len(sys.argv)):
        arr.append(sys.argv[i])
    if os.path.exists("add_item.json"):
        prev_arr = load_from_json_file("add_item.json")
        prev_arr.extend(arr)
        arr = prev_arr[:]
    save_to_json_file(arr, "add_item.json")
