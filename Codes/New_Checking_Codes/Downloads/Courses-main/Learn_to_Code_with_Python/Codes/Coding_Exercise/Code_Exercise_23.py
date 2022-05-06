# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:45:49 2021
@author: ramesh.kp

23.	1.	Define an only_evens function that accepts a list of numbers. 
		It should return a new list consisting of only the even numbers from the original list.
		EXAMPLES
		--------
		only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
		only_evens([1, 3, 5])              => []
		only_evens([])                     => []
	2.	Define a long_strings function that accepts a list of strings. 
		It should return a new list consisting of only the strings that have 5 characters or more.
		EXAMPLES
		--------
		long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
		long_strings(["Ace", "Cat", "Job"])        => []
		long_strings([])                           => []
"""

print()
print("#" * 30)
def only_evens(number_list):
	return [i for i in number_list if not i % 2]

def long_strings(string_list):
    return [i for i in string_list if len(i) >= 5]

print(only_evens([4, 8, 15, 16, 23, 42]))
print(only_evens([1, 3, 5]))
print(only_evens([]))
print("#" * 30)       
print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]))
print(long_strings([]))
print("#" * 30)
print()
