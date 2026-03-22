#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    correct_digits = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            correct_digits.append(True)
        else:
            correct_digits.append(False)

    return (correct_digits)
