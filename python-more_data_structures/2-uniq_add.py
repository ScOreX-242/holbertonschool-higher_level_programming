#!/usr/bin/python3

def uniq_add(my_list=[]):
    b = set(my_list)
    summa = 0
    for i in b:
        summa += i
    return summa
