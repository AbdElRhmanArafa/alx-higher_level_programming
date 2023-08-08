#!/usr/bin/python3
for i in range(9):
    for x in range(i, 10):
        if x == i:
            continue
        print("{:d}{:d}".format(i, x), end=", " if i != 8 else "\n")
