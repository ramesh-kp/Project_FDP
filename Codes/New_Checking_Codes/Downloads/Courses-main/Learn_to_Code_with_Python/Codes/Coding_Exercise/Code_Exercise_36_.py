# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:18:40 2021
@author: ramesh.kp

36.	Declare a delete_keys function that accepts two arguments: a dictionary and a list of strings. 
	For each string in the list, if the string exists as a dictionary key, delete the key-value pair from the dictionary. 
	If the string does not exist as a dictionary key, avoid an error. 
	The return value should be the modified dictionary object.
	EXAMPLES
	--------
	my_dict = {"A": 1, "B": 2, "C": 3}
	strings = ["A", "C"]
	delete_keys(my_dict, strings) => {'B': 2}
"""

print()
print("#" * 30)

my_dict = {"A": 1, "B": 2, "C": 3}
strings = ["A", "C"]

def delete_keys(my_dict, strings):
	for i in strings:
		if i in my_dict:
			my_dict.pop(i)
	return my_dict

print(delete_keys(my_dict, strings))
print("#" * 30)
print()
