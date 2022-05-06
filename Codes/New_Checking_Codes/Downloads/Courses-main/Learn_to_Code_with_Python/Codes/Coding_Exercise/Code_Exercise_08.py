# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:11:15 2021
@author: ramesh.kp

8.	1.	Define a vowel_count function that accepts a string argument.
		The function should return the count of vowels in the string.
		The 5 vowels are "a", "e", "i", "o", and "u".
		You can assume the string will be in all lowercase.
		EXAMPLES
		--------
		vowel_count("estate")        => 3
		vowel_count("helicopter")    => 4
		vowel_count("ssh")           => 0
	2.	Define a find_my_letter function that accepts two arguments: a string and a character.
		The function should return the first index position of the character in the string.
		The function should return a -1 if the character does not exist in the string.
		EXAMPLES
		--------
		find_my_letter("dangerous", "a")    => 1
		find_my_letter("bazooka", "z")      => 2
		find_my_letter("lollipop", "z")     => -1
"""

print()
print("#" * 30)
def vowel_count(string):
    # count = 0
    # for i in string:
    #     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
    #         count += 1
    # return count
    return string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")

def find_my_letter(string, character):
    return string.find(character)
    
print(vowel_count("estate"))
print(vowel_count("helicopter"))
print(vowel_count("ssh"))
print("#" * 30)
print(find_my_letter("dangerous", "a"))
print(find_my_letter("bazooka", "z"))
print(find_my_letter("lollipop", "z"))
print("#" * 30)
print()
