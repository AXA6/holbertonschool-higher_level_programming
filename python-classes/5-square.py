#!/usr/bin/python3
"""
Module defines a class square with a private instance attribute size
"""


class Square:
    """
    Defines a class Square that defines a square by: (based on 4-square.py)
    """
    def __init__(self, size=0):
        """
        Initialize a Square.
        Args:
            size (int, optional): The size to the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size to the square.
        Returns:
            int: The size to the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size to the square.
        Args:
            value (int): The size to the square.
        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public instance method.
        Returns:
            int: The current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints in stdout the square with the character #
        or size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
