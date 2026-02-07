#!/usr/bin/python3
"""overite file from txt and return the number of characters"""


def write_file(filename="", text=""):
    """def write file"""

    with open(filename, "w", encoding="utf-8") as f:
        """with open"""
        data_file = f.write(text)
        return data_file
