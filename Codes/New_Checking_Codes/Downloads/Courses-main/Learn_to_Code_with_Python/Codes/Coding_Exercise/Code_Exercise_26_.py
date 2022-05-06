# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:38:30 2021
@author: ramesh.kp

26.	Define an encrypt_message function that accepts a string.
	The input string will consist of only alphabetic characters.
	The function should return a string where all characters have been moved "up" two spots in the alphabet. 
	For example, "a" will become "c".
	EXAMPLES
    --------
	encrypt_message("abc") => "cde"
	encrypt_message("xyz") => "zab"
	encrypt_message("")    => ""
"""

print()
print("#" * 30)
def encrypt_message(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for i in string:
        # 26 characters in  alphabets
        # 
        encrypted_letter_index_position = (alphabet.index(i) + 2) % 26
        encrypted += alphabet[encrypted_letter_index_position]
    return encrypted

print(encrypt_message("abc"))
print(encrypt_message("xyz"))
print(encrypt_message(""))
print("#" * 30)
print()
