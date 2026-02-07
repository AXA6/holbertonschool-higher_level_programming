#!/usr/bin/python3
"""function that creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """def load from json file"""

    with open(filename, "r", encoding="utf-8") as f:
        """with open"""
        return json.load(f)
