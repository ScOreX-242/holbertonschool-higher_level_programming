#!/usr/bin/python3

def element_at(my_list, idx):
	if idx < 0:
		print("Element at index {:d} is None".format(idx))
	elif idx > len(my_list):
		print("Element at index {:d} is None".format(idx))
	else:
		print("Element at index {:d} is {}".format(idx, my_list[idx]))
