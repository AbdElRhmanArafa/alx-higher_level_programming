#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortList = sorted(a_dictionary)
    for item in sortList:
        print("{}: {}".format(item, a_dictionary.get(item)))
