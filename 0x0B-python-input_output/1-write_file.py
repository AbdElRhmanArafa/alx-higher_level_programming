#!/usr/bin/python3
"""function that writes a string to a text file """


def write_file(filename="", text=""):
    """Add a string to a text file """
    with open(filename, 'w', encoding="utf-8") as Writer:
        return Writer.write(text)
