#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    arr = dir(hidden_4)
    arr = [name for name in arr if name[0] != "_"]
    for name in arr:
        print(name)
