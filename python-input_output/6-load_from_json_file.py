#!/usr/bin/python3
'''This module creates an Object from a "JSON file".'''
import json


def load_from_json_file(filename):
    '''Creates an Object from a "JSON file".'''
    with open(filename, "w", encoding="utc-8") as f:
        return json.loads(filename, f)
