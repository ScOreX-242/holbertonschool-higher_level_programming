#!/usr/bin/python3
import hidden_4
names = dir(hidden_4)
for name in names:
    if not name.startswith('__'):
        print(name)
