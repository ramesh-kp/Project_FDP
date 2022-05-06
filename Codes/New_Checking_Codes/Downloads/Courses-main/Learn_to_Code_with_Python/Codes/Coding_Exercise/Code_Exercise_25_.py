# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:20:46 2021
@author: ramesh.kp

25.	1.	Declare a delete_all function that accepts a list of strings and a target string.
		Remove all occurrences of the target string from the list and return it.
		EXAMPLES
		--------
		delete_all([1, 3, 5], 3)  => [1, 5]
		delete_all([5, 3, 5], 5)  => [3]
		delete_all([4, 4, 4], 4)  => []
		delete_all([4, 4, 4], 6)  => [4, 4, 4]
	2.	Declare a push_or_pop function that accepts a list of numbers.
		Build up and return a new list by iterating over the list of numbers.
		If a number is greater than 5, add it to the end of the new list.
		If a number is less than or equal to 5, remove the last element added to the new list.
		Assume the order of numbers in the argument will never require removing from an empty list.
		EXAMPLES
		--------
		push_or_pop([10])            => [10]
		push_or_pop([10, 4])         => []
		push_or_pop([10, 20, 30])    => [10, 20, 30]
		push_or_pop([10, 20, 2, 30]) => [10, 30]
"""

print()
print("#" * 30)
def delete_all(string_list, string):
    while string in string_list:
        string_list.remove(string)
    return string_list

def push_or_pop(number_list):
    results = []
    for i in number_list:
        if i > 5:
            results.append(i)
        else:
            results.pop()
    return results

print(delete_all([1, 3, 5], 3))
print(delete_all([5, 3, 5], 5))
print(delete_all([4, 4, 4], 4))
print(delete_all([4, 4, 4], 6))
print("#" * 30)
print(push_or_pop([10]))
print(push_or_pop([10, 4]))
print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))
print("#" * 30)
print()
