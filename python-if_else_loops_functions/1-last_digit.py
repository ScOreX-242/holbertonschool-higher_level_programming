#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of"
last_digit = number % 10
if last_digit > 5:
    print("{0} {1} is greater than 5".format(string, number))
elif last_digit == 0:
    print("{0} {1} is 0".format(string, number))
elif last_digit < 6 and last_digit != 0:
    print("{0} {1} is less than 6 and not 0".format(string, number))
