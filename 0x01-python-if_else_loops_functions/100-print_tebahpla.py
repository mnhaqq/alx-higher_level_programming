#!/usr/bin/python3
ascii_val = 0
for i in range(122, 96, -1):
    if i % 2 != 0:
        ascii_val = i - 32
    else:
        ascii_val = i
    print("{}".format(chr(ascii_val)), end="")
