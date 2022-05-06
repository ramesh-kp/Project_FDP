# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 12:58:29 2021
@author: ramesh.kp

14.	a.	Create an empty list and assign it to the variable "empty".
	b.	Create a list with a single Boolean — True — and assign it to the variable "active".
	c.	Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".
	d.	Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".
	e.	Declare an is_long function that accepts a single list as an argument.
		It should return True if the list has more than 5 elements, and False otherwise
"""

print()
empty = []
active = [True]
favorite_numbers = [5, 4, 3, 2, 1]
colors = ["Red", "Green", "Blue"]
def is_long(single_list):
	return True if len(single_list) > 3 else False

print(empty)
print(active)
print(favorite_numbers)
print(colors)
print()
print(is_long(empty))
print(is_long(active))
print(is_long(favorite_numbers))
print(is_long(colors))
print()
