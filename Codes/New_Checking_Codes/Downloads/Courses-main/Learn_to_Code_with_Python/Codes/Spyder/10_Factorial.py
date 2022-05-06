# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:56:28 2021
@author: ramesh.kp
"""

print()
def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)
print(factorial(5))
print("#" * 80)
print()
