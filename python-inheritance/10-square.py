#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Validates size and initializes a square instance.
    """

    def __init__(self, size):
        """
        Initialize Square with size.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
