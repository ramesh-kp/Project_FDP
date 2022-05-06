# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:08:04 2021
@author: ramesh.kp

24.	Write a factors function that accepts a positive whole number.
	It should return a list of all of the number's factors in ascending order.
	HINT: Could the range function be helpful here? Or maybe a while loop?
	EXAMPLES
	--------
	factors(1)  => [1]
	factors(2)  => [1, 2]
	factors(10) => [1, 2, 5, 10]
	factors(64) => [1, 2, 4, 8, 16, 32, 64]
"""

print()
print("#" * 30)
def factors(number):
	fact = []
	for i in range(1, number + 1):
		if number % i == 0:
			fact.append(i)
	return fact
	
print(factors(1))
print(factors(2))
print(factors(10))
print(factors(64))
print("#" * 30)
print()
