#!/usr/bin/python3
for i in range(26):
    c = chr(ord('a') + i)
    if c not in ('q', 'e'):
        print(c, end="")
print()
