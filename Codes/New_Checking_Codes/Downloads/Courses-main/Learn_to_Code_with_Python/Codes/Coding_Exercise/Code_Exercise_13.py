# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:40:55 2021
@author: ramesh.kp

13.	Define a function called "factorial" that accepts a single number as input. 
	A factorial represents the product of all numbers up to, and including, that number. 
	For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120. 
	Return the factorial calculation from your function. 
	You should NOT use any kind of loops. 
	Instead, utilize recursion. 
	Your function MUST call itself.
	EXAMPLES
	--------
	factorial(1) => 1
	factorial(2) => 2
	factorial(3) => 6
	factorial(4) => 24
	factorial(5) => 120
"""

print()
print("#" * 30)
def factorial(number):
    # fact = 1
    # while(number > 0):
    #     fact *= number
    #     number = number - 1
    # return fact
    """ Using Recursion """
    return "Sorry, factorial does not exist for negative numbers" if number < 0 \
        else 1 if number == 1 or number == 0 \
        else number * factorial(number - 1)


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(-2))
print(factorial(0))
print("#" * 30)
print()

