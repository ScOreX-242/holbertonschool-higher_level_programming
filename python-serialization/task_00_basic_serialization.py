#!/usr/bin/python3
"""This module provides tools
to convert a Python dictionary into a JSON file
and to read a JSON file back into a Python dictionary."""
import json


def serialize_and_save_to_file(data, filename):
    """Convert a dictionary to JSON format and save it into a file."""
    with open(filename, "w") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    """Read a JSON file and convert its content back into a dictionary."""
    with open(filename, "r") as f:
        data = f.read()
        return json.loads(data)
