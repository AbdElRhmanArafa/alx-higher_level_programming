#!/usr/bin/python3
class Square:
    """_summary_ ssss
    """
    def __init__(self, size=0, position=(0, 0)):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.
            position (tuple, optional): _description_. Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size

    @property
    def position(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__position

    @position.setter
    def position(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
            not isinstance(value[0], int) or not isinstance(value[1], int) or \
            value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size ** 2

    def my_print(self):
        """_summary_
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
