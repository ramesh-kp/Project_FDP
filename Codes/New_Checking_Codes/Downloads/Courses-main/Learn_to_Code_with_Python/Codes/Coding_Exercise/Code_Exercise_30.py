# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:15:19 2021
@author: ramesh.kp

30.	1.	Declare a right_words function that accepts a list of words and a number.
		Return a new list with the words that have a length equal to the number.
		Do not use list comprehension.
		EXAMPLES
		--------
		right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3)     => ['cat', 'dog', 'ace']
		right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5)     => ['heart']
		right_words([], 4)                                         => []  
	2.	Declare an only_odds function. It should accept a list of whole numbers.
		It should return a list with only the odd numbers from the original list.
		Do not use list comprehension.
		EXAMPLES
		--------
		only_odds([1, 3, 5, 6, 7, 8])      =>  [1, 3, 5, 7]
		only_odds([2, 4, 6, 8])            =>  []
	3.	Declare a count_of_a function that accepts a list of strings.
		It should return a list with counts of how many “a” characters appear per string.
		Do not use list comprehension.
		EXAMPLES
		--------
		count_of_a(["alligator", "aardvark", "albatross"])    => [2, 3, 2]
		count_of_a(["plywood"])                               => [0]
		count_of_a([])                                        => []
"""

print()
print("#" * 30)
def right_words(string_list, number):
    return list(filter(lambda i: len(i) == number, string_list))

def only_odds(number_list):
    return list(filter(lambda i: i % 2, number_list))

def count_of_a(string_list):
    return list(map(lambda i: i.count("a"), string_list))

print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))
print(right_words([], 4))
print("#" * 30)
print(only_odds([1, 3, 5, 6, 7, 8]))
print(only_odds([2, 4, 6, 8]))
print("#" * 30)
print(count_of_a(["alligator", "aardvark", "albatross"]))
print(count_of_a(["plywood"]))
print(count_of_a([]))
print("#" * 30)
print()
