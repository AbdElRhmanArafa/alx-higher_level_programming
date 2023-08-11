#!/usr/bin/python3
import hidden_4


def discovr_dir():
    name_dir = dir(hidden_4)
    for i in name_dir:
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    discovr_dir()