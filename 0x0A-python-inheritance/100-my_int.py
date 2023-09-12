#!/usr/bin/python3
"""
the class MyInt
"""


class MyInt(int):
    """rebel version of an integer"""
    def __eq__(self, other):
        """what was != is  =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is  !="""
        return int(self) == other