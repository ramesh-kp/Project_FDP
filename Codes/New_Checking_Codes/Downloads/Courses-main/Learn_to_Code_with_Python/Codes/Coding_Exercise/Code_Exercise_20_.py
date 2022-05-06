# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:43:00 2021
@author: ramesh.kp

20.	1.	Define an in_list function that accepts a list of strings and a separate string.
		Return the index where the string exists in the list.
		If the string does not exist, return -1.
		Do NOT use the find or index methods.
		EXAMPLES
		--------
		strings = ["enchanted", "sparks fly", "long live"]
		in_list(strings, "enchanted")  ==> 0
		in_list(strings, "sparks fly") ==> 1
		in_list(strings, "fifteen")    ==> -1
		in_list(strings, "love story") ==> -1
	2.	Define a sum_of_values_and_indices function that accepts a list of numbers. 
		It should return the sum of all of the elements along with their index values.
		EXAMPLES
		--------
		sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
		sum_of_values_and_indices([0, 0, 0, 0]) => 6
		sum_of_values_and_indices([])           => 0
"""

print()
print("#" * 30)

strings = ["enchanted", "sparks fly", "long live"]

def in_list(string_list, string):
    for index, element in enumerate(string_list):
        if element == string:
            return index
    return -1

def sum_of_values_and_indices(number_list):
    sum_char = 0
    for index, element in enumerate(number_list):
        sum_char += index + element
    return sum_char
        
print(in_list(strings, "enchanted"))
print(in_list(strings, "sparks fly"))
print(in_list(strings, "fifteen"))
print(in_list(strings, "love story"))
print("#" * 30)
print(sum_of_values_and_indices([1, 2, 3]))
print(sum_of_values_and_indices([0, 0, 0, 0]))
print(sum_of_values_and_indices([]))
print("#" * 30)
print()
