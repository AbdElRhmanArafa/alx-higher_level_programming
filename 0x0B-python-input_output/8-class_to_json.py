#!/usr/bin/python3
"""dictionary description with simple data structure  for JSON"""


def class_to_json(obj):
    """for JSON"""
    return obj.__dict__
