# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:42:48 2021
@author: ramesh.kp

9.	Define a fancy_cleanup function that accepts a single string argument.
	The function should clean up the whitespace on both sides of the argument. 
    It should also replace every occurrence of the letter "g" with the letter "z" and every occurence of a space with an exclamation point (!).
	EXAMPLES
	--------
	fancy_cleanup("       geronimo crikey  ")   => "zeronimo!crikey"
	fancy_cleanup("       nonsense  ")          => "nonsense"
	fancy_cleanup("grade")                      => "zrade"
"""

print()
print("#" * 30)
def fancy_cleanup(string):
    return string.strip().replace("g", "z").replace(" ", "!")

print(fancy_cleanup("       geronimo crikey  "))
print(fancy_cleanup("       nonsense  "))
print(fancy_cleanup("grade"))
print("#" * 30)
print()
