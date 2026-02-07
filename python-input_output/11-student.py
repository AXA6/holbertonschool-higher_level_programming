#!/usr/bin/python3
""" function class Student that defines a student by"""


class Student:
    """define class Student"""

    def __init__(self, first_name, last_name, age):
        """def init"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """def class to json"""
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """def reload from json with key, value, self"""
        for k, v in json.items():
            setattr(self, k, v)
