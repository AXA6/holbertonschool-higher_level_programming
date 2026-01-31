#!/usr/bin/python3
""" Function that returns the list of available attributes
        and methods of an object

    Args:
        obj: instance of the class
    """


def lookup(obj):
    """ Returns:
        List of attributes """

    return dir(obj)
