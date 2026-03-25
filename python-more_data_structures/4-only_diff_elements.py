#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_3 = set_1 ^ set_2
    return set_3

# dictionary1 = []
# for item1 in set_1:
#     if item1 not in set_2:
#         dictionary1.append(item1)
# for item2 in set_2:
#     if item2 not in set_1:
#         dictionary1.append(item2)
# print(dictionary1)

# def only_diff_elements(set_1, set_2):
#     return (set_1 | set_2) - (set_1 & set_2)
