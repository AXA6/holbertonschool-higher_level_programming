#!/usr/bin/python3
"""
4-print_square module.

This module provides a function that prints a square made of the # character.
"""


def print_square(size):
    """
    Prints a square of size 'size' using the '#' character.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
