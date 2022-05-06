# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 12:23:22 2021
@author: ramesh.kp

12.	1.	Define a divisible_by_three_and_four function that accepts a number as its argument. 
		It should return True if the number is evenly divisible by both 3 and 4 . 
		It should return False otherwise.
		EXAMPLES
		--------
		divisible_by_three_and_four(3)   => False
		divisible_by_three_and_four(4)   => False
		divisible_by_three_and_four(12)  => True
		divisible_by_three_and_four(18)  => False
		divisible_by_three_and_four(24)  => True
	2.	Declare a string_theory function that accepts a string as an argument.
		It should return True if the string has more than 3 characters and starts with a capital “S”. 
		It should return False otherwise.
		EXAMPLES
		--------
		string_theory("Sansa") => True
		string_theory("Story") => True
		string_theory("See") => False
		string_theory("Fable") => False
"""

print()
print("#" * 30)
def divisible_by_three_and_four(number):
	return False if number % 3 or number % 4 else True

def string_theory(string):
	return True if len(string) > 3 and string[0] == "S" else False

print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(4))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(18))
print(divisible_by_three_and_four(24))
print("#" * 30)
print(string_theory("Sansa"))
print(string_theory("Story"))
print(string_theory("See"))
print(string_theory("Fable"))
print("#" * 30)
print()
