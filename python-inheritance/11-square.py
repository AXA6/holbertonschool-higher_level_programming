#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Represents a square using a single size value.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: Formatted string [Square] size/size
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
