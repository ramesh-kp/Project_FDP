# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:55:30 2021
@author: ramesh.kp

7.	1.	Define a first_three_characters function that accepts a string argument.
		The function should return the first 3 characters of the string.
		EXAMPLES
		--------
		first_three_characters("dynasty")   => "dyn"
		first_three_characters("empire")    => "emp"
	2.	Define a last_five_characters function that accepts a string argument. 
		The function should return the last 5 characters of the string.
		EXAMPLES
		--------
		last_five_characters("dynasty")   => "nasty"
		last_five_characters("empire")    => "mpire"
	3.	Define a is_palindrome function that accepts a string argument. 
		The function should return True if the string is spelled the same backwards as it is forwards. 
		Return False otherwise.
		EXAMPLES
		--------
		is_palindrome("racecar")   => True
		is_palindrome("yummy")     => False
"""

print()
print("#" * 30)
def first_three_characters(string):
    return string[:3]

def last_five_characters(string):
    return string[-5:]

def is_palindrome(string):
    return string == string[::-1]
    
print(first_three_characters("dynasty"))
print(first_three_characters("empire"))
print("#" * 30)
print(last_five_characters("dynasty"))
print(last_five_characters("empire"))
print("#" * 30)
print(is_palindrome("racecar"))
print(is_palindrome("yummy"))
print("#" * 30)
print()
