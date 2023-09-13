#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """append a string to a text file """
    with open(filename, 'a', encoding="utf-8") as Writer:
        return Writer.write(text)
