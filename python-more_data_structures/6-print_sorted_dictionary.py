#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = []
    for k in a_dictionary.items():
        keys.append(k)
    keyss = sorted(keys)
    for i,v in keyss:
        print("{}: {}".format(i,v))
