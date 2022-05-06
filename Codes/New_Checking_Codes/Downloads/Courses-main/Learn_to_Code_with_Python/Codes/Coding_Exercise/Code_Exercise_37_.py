# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:30:03 2021
@author: ramesh.kp

37.	1.	Declare an invert function that accepts a dictionary object. 
		The function should return a new dictionary where the keys and values from the original dictionary are inverted. 
		Each key should now be a value, and each value should be a key. 
		Assume both the keys and values of the dictionary are immutable.
		EXAMPLES
		--------
		my_dict = {"A": "B", "C": "D", "E": "F"}
		invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}
	2.	Declare a count_of_value function that accepts a dictionary and an integer.
		It should return a count of the number of times the integer appears as a value among the dictionary’s values.
		EXAMPLES
		--------
		my_dict = { "a" : 5, "b" : 3, "c" : 5 }
		count_of_value(my_dict, 5) => 2
		count_of_value(my_dict, 3) => 1
	3.	Declare a sum_of_values function that accepts a dictionary and a list of strings.
		The dictionary will have keys of strings and values of numbers.
		The function should return the sum of values for dictionary keys that are also found in the list.
		NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
		EXAMPLES
		--------
		my_dict = { "a": 5, "b": 3, "c": 10 }
		sum_of_values(my_dict, ["a"])            => 5
		sum_of_values(my_dict, ["a", "c"])       => 15
		sum_of_values(my_dict, ["a", "c", "b"])  => 18
		sum_of_values(my_dict, ["z"])            => 0
"""

print()
print("#" * 30)

my_dict_first = {"A": "B", "C": "D", "E": "F"}
my_dict_second = { "a" : 5, "b" : 3, "c" : 5 }
my_dict_third = { "a": 5, "b": 3, "c": 10 }

def invert(my_dict):
	result = {}
	for key, value in my_dict.items():
		result[value] = key
	return result

def count_of_values(dictionary, value):
	count = 0
	for k, v in dictionary.items():
		if v == value:
			count += 1
	return count

def sum_of_values(dictionary, keys):
	total = 0
	for key, value in dictionary.items():
		if key in keys:
			total += value
	return total

print(invert(my_dict_first))
print("#" * 30)
print(count_of_values(my_dict_second, 5))
print(count_of_values(my_dict_second, 3))
print("#" * 30)
print(sum_of_values(my_dict_third, ["a"]))
print(sum_of_values(my_dict_third, ["a", "c"]))
print(sum_of_values(my_dict_third, ["a", "c", "b"]))
print(sum_of_values(my_dict_third, ["z"]))
print("#" * 30)
print()
