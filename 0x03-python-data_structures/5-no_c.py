#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for char_C in my_string:
        if char_C != 'c' and char_C != "C":
            new_str += char_C
    return new_str
