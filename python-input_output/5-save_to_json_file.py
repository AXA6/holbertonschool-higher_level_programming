#!/usr/bin/python3
"""fonction that directly serialize in python object"""
import json


def save_to_json_file(my_obj, filename):
    """def save to json file"""
    with open(filename, "w", encoding="utf-8") as f:
        """with open"""
        json.dump(my_obj, f)
