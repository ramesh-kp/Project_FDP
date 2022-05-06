# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:39:34 2021
@author: ramesh.kp

34.	a.	Create an empty dictionary and assign it to the variable empty.
	b.	Create a dictionary with three key-value pairs. 
		The keys should be strings and the values should be integer values. 
		Assign the dictionary to a my_dict variable.
	c.	A dictionary’s keys can be any immutable data structure. 
		Create a dictionary with two key-value pairs and assign it to a winning_lottery_numbers variable. 
		Both of the keys should be tuples. 
		One of the values should be True, the other value should be False.
"""

print()
print("#" * 30)
empty = {}
print(empty)
print("#" * 30)

my_dict = {"Boris": 29, "Abe": 45, "Debbie": 42}
print(my_dict)
print("#" * 30)

winning_lottery_numbers = {(4, 8, 15, 16, 23, 42): True, (6, 12, 14): False}
print(winning_lottery_numbers)
print("#" * 30)
print()
