#!/usr/bin/python3
'''This module  returns the dictionary description.'''


def class_to_json(obj):
    '''returns the dictionary description.'''
    return obj.__dict__
