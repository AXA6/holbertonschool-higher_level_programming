#!/usr/bin/python3
"""
Module defines BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """
    BaseGeometry class - serves as base class for geometry objects.
    """

    def area(self):
        """
        Public instance method that raises an exception.

        Raises:
            Exception: Indicates that area() is not implemented.
        """
        raise Exception('area() is not implemented')
