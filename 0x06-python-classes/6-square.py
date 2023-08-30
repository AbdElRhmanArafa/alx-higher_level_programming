#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    This class represents a simple square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Args:
        size (int): The size of the square (default 0).
        position (tuple): The position of the square (default (0, 0)).

    Raises:
        TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
        ValueError: If size or position values are less than 0.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square (default 0).
            position (tuple, optional): The position of the square (default (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size or position values are less than 0.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If position values are less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
            not isinstance(value[0], int) or not isinstance(value[1], int) or \
            value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character and with an offset defined by position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
