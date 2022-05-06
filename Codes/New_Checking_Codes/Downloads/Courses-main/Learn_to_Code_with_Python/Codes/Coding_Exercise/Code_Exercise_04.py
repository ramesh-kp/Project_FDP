# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 17:14:04 2021
@author: ramesh.kp

4.	1.	Define a string_adder function that accepts two strings (a and b) as arguments. 
		It should return a concatenated version of the arguments with a space in between.
		If the user does not pass in arguments, both arguments should default to an empty string.
		EXAMPLES
		--------
		string_adder("Hello", "World")      => "Hello World"
		string_adder("Emilio", "Estevez")   => "Emilio Estevez"
		string_adder()                      => " "
		string_adder("Tiger")               => "Tiger "
	2.	Define a multiplier function that accepts three integers as arguments.
		Return the product of the arguments. 
		The product is the total when values are multiplied together.
		If the user does not provide any arguments, all three parameters should have default arguments of 1.
		EXAMPLES
		--------
		multiplier(2, 2, 2)    => 8
		multiplier()           => 1
		multiplier(3)          => 3
		multiplier(2, 5)       => 10
"""

print()
print("#" * 30)
def string_adder(a = "", b = ""):
    return a + " " + b

def multiplier(first = 1, second = 1, third = 1):
	return first * second * third

print(string_adder("Hello", "World"))
print(string_adder("Emilio", "Estevez"))
print(string_adder())
print(string_adder("Tiger"))
print("#" * 30)
print(multiplier(2, 2, 2))
print(multiplier())
print(multiplier(3))
print(multiplier(2, 5))
print("#" * 30)
print()
