# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:09:38 2021
@author: ramesh.kp

44.	Define an "outer" function that accepts no arguments.
	Inside the body of "outer", define an "inner" function.
	The "inner" function should return the value 5.
	From "outer", return the uninvoked "inner" function.
"""

print()
print("#" * 30)

def outer():
    def inner():
        return 5
    return inner

print(outer()())
print("#" * 30)
print()
