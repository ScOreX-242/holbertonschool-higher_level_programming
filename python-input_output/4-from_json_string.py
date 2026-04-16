#!/usr/bin/python3
'''This module returns json to object'''
import json


def from_json_string(my_str):
    '''Returns json to object'''
    return json.loads(my_str)
