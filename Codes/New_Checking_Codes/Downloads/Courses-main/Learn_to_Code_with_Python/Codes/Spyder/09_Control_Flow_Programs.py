# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:47:30 2021
@author: ramesh.kp
"""

print()
def even_or_odd(number):
    if number % 2:
        return "Odd"
    else:
        return "Even"
print(even_or_odd(2))
print(even_or_odd(31))
print("#" * 80)

def odd_or_even(number):
    return "Odd" if number % 2 else "Even"
print(odd_or_even(2))
print(odd_or_even(31))
print("#" * 80)

value = 95
if 90 < value < 100:
    print("This is the shortcut method")
print("#" * 80)

# Recursion Method
def count_down_from(number):
    if number <= 0:
        return
    print(number)
    count_down_from(number - 1)
count_down_from(10)
print("#" * 80)

def reverse(str):
    if len(str) <= 1:
        return str
    return str[-1] + reverse(str[:-1])
print(reverse("Ramesh K P"))
print("#" * 80)

# Without using recursion
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[::-1])
name = "Ramesh k P"
print(name[::-1])
print()




















