#!usr/bin/python3
"""A custom list class that inherits from the built-in list class."""


class MyList(list):
    """print sorted list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
