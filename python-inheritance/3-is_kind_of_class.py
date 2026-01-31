#!/usr/bin/python3
"""
This module defines a function that checks if an object is
an instance of a class or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if `obj` is the same class or inherits from `a_class`.

    Args:
        obj (any): The object to compare.
        a_class (type): The class to compare with.

    Returns:
        bool: True if the object is an instance or inherits from
        the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
