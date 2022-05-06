# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:11:19 2021
@author: ramesh.kp

17.	1.	Declare a nested_extraction function that accepts a list of lists and an index position.
		The function should use the index as the basis of finding both the nested list and the element from that list with the given index position.
		You can assume the number of lists will always be equal to the number of elements within each of them.
		EXAMPLES
		--------
		nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
		nested_extraction(nl, 0)  => 3
		nested_extraction(nl, 1)  => 8
		nested_extraction(nl, 2)  => 12
	2.	Declare a beginning_and_end function that accepts a list of elements.
		It should return True if the first and last elements in the list are equal and False if they are unequal.
		Assume the list will always have at least 1 element.
		EXAMPLES
		--------
		beginning_and_end([1, 2, 3, 1])     => True
		beginning_and_end([1, 2, 3, 4, 5])  => False
		beginning_and_end(["a", "b", "a"])  => True
		beginning_and_end([15])             => True
	3.	Declare a long_word_in_collection function that accepts a list and a string. 
		The function should return True if 
		- the string exists in the list AND
		- the string has more than 4 characters.
		EXAMPLES
		--------
		words = ["cat", "dog", "rhino"]
		long_word_in_collection(words, "rhino")  => True
		long_word_in_collection(words, "cat")    => False
		long_word_in_collection(words, "monkey") => False
"""

print()
print("#" * 30)

nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
words = ["cat", "dog", "rhino"]

def nested_extraction(string_list, index):
    return string_list[index][index]

def beginning_and_end(string_list):
    return string_list[0] == string_list[-1]

def long_word_in_collection(string_list, string):
    return string in string_list and len(string) > 4

print(nested_extraction(nl, 0))
print(nested_extraction(nl, 1))
print(nested_extraction(nl, 2))
print("#" * 30)
print(beginning_and_end([1, 2, 3, 1]))
print(beginning_and_end([1, 2, 3, 4, 5]))
print(beginning_and_end(["a", "b", "a"]))
print(beginning_and_end([15]))
print("#" * 30)
print(long_word_in_collection(words, "rhino"))
print(long_word_in_collection(words, "cat"))
print(long_word_in_collection(words, "monkey"))
print("#" * 30)
print()
