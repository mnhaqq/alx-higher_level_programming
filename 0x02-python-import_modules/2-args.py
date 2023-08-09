#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    num_args = len(args)
    if num_args == 1:
        print(f"0 arguments.")
    elif num_args == 2:
        print(f"1 argument:")
    else:
        print(f"{num_args-1} arguments:")

    for i in range(1, num_args):
        print(f"{i}: {args[i]}")
