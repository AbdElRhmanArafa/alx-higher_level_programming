#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    This class represents a simple square.

    Attributes:
        size (int): The size of the square.

    Args:
        size (int): The size of the square (default 0).

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")
        self.__size = size
