# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:49:14 2021
@author: ramesh.kp

38.	Declare a common_elements function that accepts a dictionary.
	It should return a list with all of the elements that are found as both a key and a value in the dictionary.
	HINT: Use the in operation to check for inclusion in a view or list object
	EXAMPLES
	--------
	my_dict = {"A": "K", "B": "D", "C": "A", "D": "Z"}
	common_elements(my_dict) => ["A", "D"]
"""

print()
print("#" * 30)

my_dict = {"A": "K", "B": "D", "C": "A", "D": "Z"}

def common_elements(my_dict):
    return [key for key in my_dict.keys() if key in my_dict.values()]

print(common_elements(my_dict))
print("#" * 30)
print()
