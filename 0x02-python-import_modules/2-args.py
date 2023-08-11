#!/usr/bin/python3
import sys
def priny_args():
    arg_list = sys.argv

    num_arguments = len(arg_list) - 1

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    for index, value in enumerate(arg_list[1:], start=1):
        print("{}: {}".format(index, value))
if __name__ == "__main__":
    priny_args()
