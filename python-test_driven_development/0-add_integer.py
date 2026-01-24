#!/usr/bin/python3
"""
0-add_integer module.

This module provides a function that adds two integers with validation.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a (int|float): The first number.
        b (int|float): The second number (default is 98).

    Returns:
        int: The sum of a and b after casting to integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
