# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:38:09 2021
@author: ramesh.kp

31.	1.	Declare a greater_sum function that accepts two lists of numbers. 
		It should return the list with the greatest sum.
		You can assume the lists will always have different sums.
		EXAMPLES
		--------
		greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
		greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
		greater_sum([1], [])              => [1]
	2.	Declare a sum_difference function that accepts two lists of numbers.
		It should return the difference between the sum of values in the first list and the second list.
		EXAMPLES
		--------
		sum_difference([1, 2, 3], [1, 2, 4]) => 6 - 7 => -1
		sum_difference([4, 5], [2, 3, 6])    => 9 - 11 => -2
		sum_difference([1], [])              => 1
"""

print()
print("#" * 30)
def greater_sum(first_list, second_list):
	return first_list if sum(first_list) > sum(second_list) else second_list

def sum_difference(first_list, second_list):
    return sum(first_list) - sum(second_list)

print(greater_sum([1, 2, 3], [1, 2, 4]))
print(greater_sum([4, 5], [2, 3, 6]))
print(greater_sum([1], []))
print("#" * 30)
print(sum_difference([1, 2, 3], [1, 2, 4]))
print(sum_difference([4, 5], [2, 3, 6]))
print(sum_difference([1], []))
print("#" * 30)
print()
