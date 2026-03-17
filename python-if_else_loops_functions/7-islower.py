#!/usr/bin/python3
def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        print("{} is lower".format(chr(c)))
        return True
    elif ord(c) > 64 and ord(c) < 91:
        print("{} is upper".format(chr(c)))
        return False
