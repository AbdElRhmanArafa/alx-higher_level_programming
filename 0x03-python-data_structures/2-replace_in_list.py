#!/usr/bin/python3
def replace_in_list(my_lsit, idx, element):
    if 0 <= idx <= len(my_lsit):
        my_lsit[idx] = element
    else:
        return my_lsit

