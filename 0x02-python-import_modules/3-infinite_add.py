#!/usr/bin/python3

def infinite_add(args):
    total_sum = 0
    for value in args[1:]:
        total_sum += int(value)
    return total_sum


if __name__ == "__main__":
    import sys
    args = sys.argv
    result = infinite_add(args)
    print(result)
