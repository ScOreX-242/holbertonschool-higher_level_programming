#!/usr/bin/python3
'''This module writes to text file.'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes to text file.'''
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
