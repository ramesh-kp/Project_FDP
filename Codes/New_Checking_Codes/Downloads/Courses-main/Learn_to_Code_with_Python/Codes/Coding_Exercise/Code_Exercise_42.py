# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:05:22 2021
@author: ramesh.kp

42.	1.	Declare a set with 3 of your favorite movies as strings.
		Assign it to a movies variable.
	2.	Declare a set with the first four months of the year as strings.
		Assign it to a months variable.
		Make sure the first letter of each month is capitalized.
	3.	Create an empty set and assign it to an empty variable.
	4.	Define a remove_duplicates function that accepts a single list as an argument. 
		The function should return a list with all of the duplicates from the original list removed.
		The order of elements in the returned list is irrelevant.
		EXAMPLES
		--------
		remove_duplicates([1, 2, 1, 2])  => [1, 2] or [2, 1]
		remove_duplicates([1, 2, 3, 4])  => [1, 2, 3, 4] in some order
"""

print()
print("#" * 30)

movies = {"Commando", "Die Hard", "Memento"}
months = {"January", "February", "March", "April"}
empty = set()

def remove_duplicates(elements):
    return list(set(elements))

print(movies)
print("#" * 30)
print(months)
print("#" * 30)
print(empty)
print("#" * 30)
print(remove_duplicates([1, 2, 1, 2]))
print(remove_duplicates([1, 2, 3, 4]))
print("#" * 30)
print()
