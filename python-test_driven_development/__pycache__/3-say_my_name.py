#!/usr/bin/python3
"""
3-say_my_name module.

This module provides a function that prints a name in the format:
My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name.

    Args:
        first_name (str): First name of the person.
        last_name (str): Last name of the person (optional).

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
