#!/usr/bin/python3
"""Student Class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """convert to json
        # Create a dictionary comprehension that iterates through
         the attributes
        # listed in attrs and includes them in the result only
         if they exist in the object.
        """
        if type(attrs) == list and all(type(val) == str for val in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
