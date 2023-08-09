#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ans = 0
    args = sys.argv
    num_args = len(args)

    for i in range(1, num_args):
        ans += int(args[i])
    print(ans)
