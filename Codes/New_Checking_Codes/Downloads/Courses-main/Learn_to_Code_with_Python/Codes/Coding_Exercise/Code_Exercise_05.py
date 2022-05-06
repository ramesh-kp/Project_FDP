# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:39:58 2021
@author: ramesh.kp

5.	1.	Define a long_word function that accepts a string. 
		The function should return a Boolean that reflects whether the string has more than 7 characters.
		EXAMPLES
		--------
		long_word("Python")         => False
		long_word("magnificent")    => True
	2.	Define a first_longer_than_second function that accepts two string arguments. 
		The function should return a True if the first string is longer than the second and False otherwise (including if they are equal in length).
		EXAMPLES
		--------
		first_longer_than_second("Python", "Ruby")     => True
		first_longer_than_second("cat", "mouse")       => False
		first_longer_than_second("Steven", "Seagal")   => False
"""

print()
print("#" * 30)
def long_word(string):
    return len(string) > 7

def first_longer_than_second(first, second):
    return len(first) > len(second)

print(long_word("Python"))
print(long_word("Magnificent"))
print("#" * 30)
print(first_longer_than_second("Python", "Ruby"))
print(first_longer_than_second("cat", "mouse"))
print(first_longer_than_second("Steven", "Seagal"))
print("#" * 30)
print()
