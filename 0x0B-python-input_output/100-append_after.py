#!/usr/bin/python3
"""Defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file."""
    text = ""
    with open(filename) as reader:
        for line in reader:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as writer:
        writer.write(text)
