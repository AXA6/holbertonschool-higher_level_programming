#!/usr/bin/env python3
"""import pickle"""

import pickle


class CustomObject:
    """def class CustomObject"""

    def __init__(self, name, age, is_student):
        """initialize name, age, is student from CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the class CustomObject"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serializable an object from using pickle"""
        try:
            with open(filename, "wb") as f:
                return pickle.dump(self, f)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """deserializable an object from using pickle"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
