# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:48:35 2021
@author: ramesh.kp

3.	a.	Define a easy_money function that accepts no parameters and always returns the value 100.
	b.	Define a best_food_ever function that accepts no parameters and always returns the string “Sushi”.
	c.	Define a convert_to_currency function that accepts a single parameter (an integer). 
		The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
		EXAMPLES
		--------
		convert_to_currency(15)    => "$15"
		convert_to_currency(8)     => "$8"
"""

print()
print("#" * 30)
def easy_money():
    return 100

def best_food():
    return "Sushi"

def convert_to_currency(integer):
    return "$" + str(integer)

print(easy_money())
print("#" * 30)
print(best_food())
print("#" * 30)
print(convert_to_currency(15))
print(convert_to_currency(8))
print("#" * 30)
print()
