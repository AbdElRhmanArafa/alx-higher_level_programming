#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    operator = ['+', '-', '*', '/']
    result = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    for index, i in enumerate(operator):
        print("{:d} {:s} {:d} = {:d}".format(a, i, b, result[index]))
