#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of"
last_digit = abs(number) % 10
third_type = "and is less than 6 and not 0"
first_type = "and is greater than 5"
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    print("{0} {1} is {2} {3}".format(string, number, last_digit, first_type))
elif last_digit == 0:
    print("{0} {1} is 0 and is 0".format(string, number))
elif last_digit < 6 and last_digit != 0:
    print("{0} {1} is {2} {3}".format(string, number, last_digit, third_type))
