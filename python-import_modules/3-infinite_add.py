#!/usr/bin/python3
import sys
if __name__ == "__main__":
    b = 0
    for i in range(1, len(sys.argv)):
        b = b + int(sys.argv[i])
    print(b)
