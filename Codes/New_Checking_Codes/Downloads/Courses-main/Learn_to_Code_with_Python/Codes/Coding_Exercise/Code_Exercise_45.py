# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:13:38 2021
@author: ramesh.kp

45.	Define a global "a" variable assigned to the value 1.
	Declare a "modify_a" function that accepts a single argument.
	It should overwrite the value of the a global variable with the argument.
"""

print()
print("#" * 30)

a = 1
def modify_a(value):
    global a
    a = value
    
print(a)
modify_a(50)
print(a)
print("#" * 30)
print()
