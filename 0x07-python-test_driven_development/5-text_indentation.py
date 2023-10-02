#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
      text: A string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = text.split(".")
    sentences += text.split("?")
    sentences += text.split(":")

    for sentence in sentences:
        sentence = sentence.strip()

        print(sentence)