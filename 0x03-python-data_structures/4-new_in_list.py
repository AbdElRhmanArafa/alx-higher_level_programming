#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for index, value in enumerate(my_list):
        if index == idx:
            new_list.append(element)
        else:
            new_list.append(value)
    return new_list
