#!/usr/bin/python3
"""This module defines a CustomObject class
and provides methods to serialize and deserialize
its instances using the pickle module."""
import pickle


class CustomObject:
    """Custom object with basic attributes and pickle support."""

    def __init__(self, name, age, is_student):
        """Initialize the object with name, age and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object and save it to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, PermissionError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load an object from a file and return it."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except (FileNotFoundError, PermissionError, pickle.PickleError, EOFError):
            return None
