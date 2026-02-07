#!/usr/bin/python3
""" function class Student that defines a student by"""


class Student:
    """define class Student"""

    def __init__(self, first_name, last_name, age):
        """def init"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """def class to json"""
        return self.__dict__
