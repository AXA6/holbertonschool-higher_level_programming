#!/usr/bin/python3

"""read file my_file.txt from 0-main.py"""


def read_file(filename=""):
    """def file name"""

    with open(filename, "r", encoding="utf-8") as f:
        """with open"""
        data_file = f.read()
        print(data_file, end="")
