#!/usr/bin/python3
"""
This module defines a function that checks if an object is exactly
an instance of the specified class (not a subclass).
"""


def is_same_class(obj, a_class):
    """
    Checks if `obj` is exactly an instance of the specified class.

    Args:
        obj (any): The object to compare.
        a_class (type): The class to compare with.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
