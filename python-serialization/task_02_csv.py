#!/usr/bin/python3
"""This module contains functionality
to transform CSV file data into JSON format."""
import csv
import json


def convert_csv_to_json(filename):
    """Read a CSV file and write its contents into a JSON file."""

    try:
        with open(filename, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True

    except Exception:
        return False
