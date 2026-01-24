#!/usr/bin/python3
"""Module for add_integer function."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: first integer or float
        b: secuond integer or float (default is 98)

    Returns:
        the addition of a and b as an integer

    Raises:
    TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
