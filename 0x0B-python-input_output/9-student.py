#!/usr/bin/python3
"""Student Class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.lastname = last_name
        self.age = age

    def to_json(self):
        """convert to json"""
        return self.__dict__
