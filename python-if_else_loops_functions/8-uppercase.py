#!/usr/bin/python3
def uppercase(str):
    for i in range(str):
        if ord(i) > 96 and ord(i) < 123:
            i = i-32
            return(i)
