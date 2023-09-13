#!/usr/bin/python3
""" returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """convert my_obj to json object"""
    json_object = json.dumps(my_obj)
    return json_object
