# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:49:12 2021
@author: ramesh.kp

40.	Declare a plenty_of_arguments function that accepts two parameters (a and b) and an additional **kwargs parameter.
	The function should return True if the sum of a, b, and the values of **kwargs is greater than 100. 
	It should return False otherwise.
	EXAMPLES
	--------
	plenty_of_arguments(20, 30)                          => False
	plenty_of_arguments(a = 50, b = 75)                  => True
	plenty_of_arguments(a = 50, b = 25, c = 50)          => True
	plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)  => False
	plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)  => True
"""

print()
print("#" * 30)
def plenty_of_arguments(a, b, **numbers):
    return a + b + sum(numbers.values()) > 100

print(plenty_of_arguments(20, 30))
print(plenty_of_arguments(a = 50, b = 75))
print(plenty_of_arguments(a = 50, b = 25, c = 50))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 25))
print(plenty_of_arguments(a = 25, b = 25, c = 25, d = 26))
print("#" * 30)
print()
