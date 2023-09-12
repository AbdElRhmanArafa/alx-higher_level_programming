#!/usr/bin/python3
"""True if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """ is instance yes or no """
    return type(obj) is a_class
