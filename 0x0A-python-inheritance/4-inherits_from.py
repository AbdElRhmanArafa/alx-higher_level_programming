#!/usr/bin/python3
"""True if the object is an instance of a class that inherited"""

def inherits_from(obj, a_class):
    """True if the object is an instance of a class that inherited"""
    if type(obj) is a_class:
        return False
    for base_class in type(obj).__bases__:
        if inherits_from(base_class, a_class):
            return True
        return False
