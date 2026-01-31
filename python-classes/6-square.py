#!/usr/bin/python3
"""
Module defines a class square with private
instance attributes size and position.
"""


class Square:
    """
    Class Square that defines a square by: (based on 5-square.py)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size to the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size to the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position to the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position to the square.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Public instance method.
        Returns:
            int: The current square area
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
