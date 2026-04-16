#!/usr/bin/python3
"""Module with Student class definition."""


class Student:
    """Represents a student object."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of the instance."""
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

        return dict(self.__dict__)

    def reload_from_json(self, json):
        """Updates attributes from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
