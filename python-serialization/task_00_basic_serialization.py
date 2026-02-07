#!/usr/bin/env python3
"""Create a basic serialization module"""

import json


def serialize_and_save_to_file(data, filename):
    """def serialize_and_save_to_file"""
    with open(filename, 'w', encoding="utf-8") as f:
        """with open"""
        json.dump(data, f, indent=2)


def load_and_deserialize(filename):
    """def load and deserialize"""
    with open(filename, "r", encoding="utf-8") as f:
        """with open"""
        data = json.load(f)
        return data
