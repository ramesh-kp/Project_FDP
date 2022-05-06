# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:05:08 2021
@author: ramesh.kp

16.	Define a split_in_two function that accepts a list and a number.
	If the number is even, return the list elements from the third element to the end of the list.
	If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive).
	EXAMPLES
	--------
	values = ["a", "b", "c", "d", "e", "f"]
	split_in_two(values, 3)     => ["a", "b"]
	split_in_two(values, 4)     => ["c", "d", "e", "f"]
	split_in_two(values, 1)     => ["a", "b"]
	split_in_two(values, 10)    => ["c", "d", "e", "f"]
"""

print()
print("#" * 30)
values = ["a", "b", "c", "d", "e", "f"]
def split_in_two(string_list, number):
	return string_list[:2] if number % 2 else string_list[2:]

print(split_in_two(values, 3))
print(split_in_two(values, 4))
print(split_in_two(values, 1))
print(split_in_two(values, 10))
print("#" * 30)
print()
