#!/usr/bin/python3
class Square:
    """_summary_
    """
    def __init__(self, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size

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
            for _ in range(self.size):
                print("#" * self.size)
