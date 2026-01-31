#!/usr/bin/python3
"""
This module defines a function that checks if an object
inherits (directly or indirectly) from a specified class,
but is not exactly an instance of that class.
"""


def inherits_from(obj, a_class):
    """
    Checks if `obj` is an instance of a subclass of `a_class`.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if `obj` is an instance of a subclass of `a_class`,
        but not an instance of `a_class` itself; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
