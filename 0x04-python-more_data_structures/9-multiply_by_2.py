#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a_dictioary = {}
    for key, value in a_dictionary:
        new_a_dictioary[key] = value * 2
    return new_a_dictioary
