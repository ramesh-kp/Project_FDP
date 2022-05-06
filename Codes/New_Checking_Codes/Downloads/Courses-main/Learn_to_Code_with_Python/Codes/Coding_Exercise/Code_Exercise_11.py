# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 12:19:14 2021
@author: ramesh.kp

11.	Declare a negative_energy function that accepts a numeric argument and returns its absolute value.
	The absolute value is the number's distance from zero.
	EXAMPLES
	--------
	negative_energy(5)    => 5
	negative_energy(10)   => 10
	negative_energy(-5)   => 5
	negative_energy(-8)   => 8
	negative_energy(0)    => 0
"""

print()
def negative_energy(number):
	return number if number >= 0 else -number

print("#" * 30)
print(negative_energy(5))
print(negative_energy(10))
print(negative_energy(-5))
print(negative_energy(-8))
print(negative_energy(0))
print("#" * 30)
print()
