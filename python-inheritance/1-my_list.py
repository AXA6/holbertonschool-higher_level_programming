#!/usr/bin/python3
"""
A module that defines a custom list class
with a method to print the list sorted in ascending order.
"""


class MyList(list):
    """
    A class that inherits from the built-in list
    and adds a method to print the sorted list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order (sorted),
        without modifying the original list.
        """
        print(sorted(self))
