#!usr/bin/python3
"""A custom list class that inherits from the built-in list class."""


class MyList(list):
    """class print sorted list"""
    def print_sorted(self):
        """ Prints sorted lists """
        sorted_list = sorted(self)
        print(sorted_list)
