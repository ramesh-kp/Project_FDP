# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 12:14:16 2021
@author: ramesh.kp

10.	1.	Define a even_or_odd function that accepts a single integer.
		If the integer is even, the function should return the string “even”.
		If the integer is odd, the function should return the string “odd”.
		EXAMPLES
		--------
		even_or_odd(2)    => "even"
		even_or_odd(0)    => "even"
		even_or_odd(13)   => "odd"
		even_or_odd(9)    => "odd"
	2.	Define a truthy_or_falsy function that accepts a single argument.
		The function should return a string that reads "The value _____ is ______". 
		where the first space is the argument and the second space is either 'truthy' or 'falsy'. 
		See the sample invocations below.
		EXAMPLES
		--------
		truthy_or_falsy(0)        => "The value 0 is falsy"
		truthy_or_falsy(5)        => "The value 5 is truthy"
		truthy_or_falsy("Hello")  => "The value Hello is truthy"
		truthy_or_falsy("")       => "The value  is falsy"
"""

print()
print("#" * 30)
def even_or_odd(string):
	return "odd" if string % 2 else "even"

def truthy_or_falsy(string):
	return "The value {} is {check}".format(string, check = "truthy" if string else "falsy")

print(even_or_odd(2))
print(even_or_odd(0))
print(even_or_odd(13))
print(even_or_odd(9))
print("#" * 30)
print(truthy_or_falsy(0))
print(truthy_or_falsy(5))
print(truthy_or_falsy("Hello"))
print(truthy_or_falsy(""))
print("#" * 30)
print()
