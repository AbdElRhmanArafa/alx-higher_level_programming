#!/usr/bin/python3
"""True if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """True if the object is an instance of a class that inherited"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
