# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:00:54 2021
@author: ramesh.kp

43.	Define an invoke_thrice function.
	It should accept a single argument (which will be a function).
	In its body, the invoke_thrice function should invoke.
	The function that's passed in exactly three times.
"""

print()
print("#" * 30)

def invoke_thrice(func):
    func()
    func()
    func()
    
def sample():
    print("Ramesh K P")
    print("Sreejisha P")
    print("Dhruv Sarang K P")
    
def another_sample():
    print("Raman Kutty K P")
    print("Shylaja E")
    
invoke_thrice(sample)
invoke_thrice(another_sample)
print("#" * 30)
print()

