# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:10:34 2021
@author: ramesh.kp

22.	1.	Declare a length_match function that accepts a list of strings and an integer.
		It should return a count of the number of strings whose length is equal to the number.
		EXAMPLES
		--------
		length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
		length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
		length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
		length_match([], 5))                                   => 0
	2.	Declare a sum_from function that accepts two numbers as arguments.
		The second number will always be greater than the first number.
		The function should return the sum of all numbers from the first number to the second number (inclusive).
		EXAMPLES
		--------
		sum_from(1, 2)   # 1 + 2                  => 3
		sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
		sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
		sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42
	3.	Declare a same_index_values function that accepts two lists.
		The function should return a list of the index positions in which the two lists have equal elements.
		EXAMPLES
		--------
		same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
		same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]
"""

print()
print("#" * 30)
def length_match(string_list, number):
    total = 0
    for i in string_list:
        if len(i) == number:
            total += 1
    return total

def sum_from(first, second):
    total = 0
    for i in range(first, second + 1):
        total += i
    return total

def same_index_values(first_list, second_list):
    output = []
    for index, element in enumerate(first_list):
        if element == second_list[index]:
            output.append(index)
    return output

print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))
print(length_match([], 5))
print("#" * 30)
print(sum_from(1, 2))
print(sum_from(1, 5))
print(sum_from(3, 8))
print(sum_from(9, 12))
print("#" * 30)
print(same_index_values([1, 2, 3], [3, 2, 1]))
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))
print("#" * 30)
print()

