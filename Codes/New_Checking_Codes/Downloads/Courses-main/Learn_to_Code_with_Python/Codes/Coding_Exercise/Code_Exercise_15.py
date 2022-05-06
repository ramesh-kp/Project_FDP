# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 13:11:57 2021
@author: ramesh.kp

15.	1.	Define a first_and_last function that accepts a list of strings. 
		The function should return a concatenation of the first element and the last element. 
		Assume the list will always have 1 or more elements.
		EXAMPLES
		--------
		first_and_last(["a", "b", "c"])        => "ac"
		first_and_last(["bob", "tom", "rob"])  => "bobrob"
		first_and_last(["a"])                  => "aa"
	2.	Define a product_of_even_indices function that accepts a list of numbers. 
		The list will always have 6 total elements. 
		The function should return the product (multiplied total) of all numbers at an even index (0, 2, 4).
		EXAMPLES
		--------
		product_of_even_indices([1, 2, 3, 4, 5, 6])    =>  15
		product_of_even_indices([3, 4, 3, 5, 3, 6])    =>  27
	3.	Define a first_letter_of_last_string function that accepts a list of strings. 
		It should return one character — the first letter of the last string in the list. 
		Assume the list will always have at least one string.
		EXAMPLES
		--------
		first_letter_of_last_string(["cat", "dog", "zebra"]) => "z"
		first_letter_of_last_string(["nonsense"]) => "n"
"""

print()
print("#" * 30)
def first_and_last(string_list):
    return string_list[0] + string_list[-1]    

def product_of_even_indices(string_list):
    return string_list[0] * string_list[2] * string_list[4]

def first_letter_of_last_string(string_list):
    return string_list[-1][0]

print(first_and_last(["a", "b", "c"]))
print(first_and_last(["bob", "tom", "rob"]))
print(first_and_last(["a"]))
print("#" * 30)
print(product_of_even_indices([1, 2, 3, 4, 5, 6]))
print(product_of_even_indices([3, 4, 3, 5, 3, 6]))
print("#" * 30)
print(first_letter_of_last_string(["cat", "dog", "zebra"]))
print(first_letter_of_last_string(["nonsense"]))
print("#" * 30)
print()
