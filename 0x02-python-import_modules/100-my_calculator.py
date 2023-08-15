#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = ["+", "-", "*", "/"]
    if args[1] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(args[0])
    b = int(args[2])
    op = args[1]

    functions = [add(a, b), sub(a, b), mul(a, b)]
    if b != 0:
        functions.append(div(a, b))

    dic = dict()
    for i in range(len(functions)):
        dic[operators[i]] = functions[i]

    print(f"{a} {op} {b} = {dic.get(op)}")
