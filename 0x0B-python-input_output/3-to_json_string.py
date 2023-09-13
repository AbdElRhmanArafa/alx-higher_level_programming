#!/usr/bin/python3
import json
""" returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """convert my_obj to json object"""
    json_object = json.dumps(my_obj)
    return json_object
