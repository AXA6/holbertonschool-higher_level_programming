#!/usr/bin/python3
"""Module that defines a Square class
"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize the square with a size (private attribute)"""
        self.size = size  # Bة

    @property
    def size(self):
        """Getter: retrieve the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: validate and update the private attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2
