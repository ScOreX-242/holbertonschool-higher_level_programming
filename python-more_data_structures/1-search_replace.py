#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for i in range (len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
        new_list.append(my_list[i])
    return new_list


