#!/usr/bin/python3

def common_elements(set_1, set_2):
    result = []
    for item1 in set_1:
        for item2 in set_2:
            if item1 == item2:
                result.append(item1)
    return result
    
# def common_elements(set_1, set_2):
#     result = set_1 & set_2
#     return result

# def common_elements(set_1, set_2):
#     common = []
#     for item in set_1:
#         if item in set_2:
#             common.append(item)
#     return common
