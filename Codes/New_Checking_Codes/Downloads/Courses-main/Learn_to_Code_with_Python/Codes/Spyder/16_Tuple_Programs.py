# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:18:20 2021
@author: ramesh.kp
"""

print()
print("#" * 30)

addresses = (
    ["Kizhakkepurath House", "Amminikkad P O", "Perinthalmanna", "Malappuram DST"],
    ["Naico", "Smartcity", "Kakkanad", "Cochi", "Ernakulam DST"]
    )
employee = ("Ramesh", "K P", "Embedded Engineer", "32")

# List in Tuples
print(addresses)
addresses[1][0] = "Naico ITS"
print(addresses)
print("#" * 30)

# Swap two numbers
first = 10
second = 20
second, first = first, second
print(first, second)

# * Destructure
# first = employee[0]
# last = employee[1]
# post = employee[-2]
# age = employee[-1]
# print(first, last, post, age)
########################################
# first, last, post, age = employee
# print(first, last, post, age)
########################################
# first, last, *details = employee
# print(first, last, details)
########################################
*details, pos, age = employee
print(details, pos, age)
print("#" * 30)

# Variable number of function arguements
def destructure_check(string, first, *numbers):
    print(string)
    print(first)
    greatest = numbers[0]
    for i in numbers:
        if i > greatest:
            greatest = i
    return greatest

print(destructure_check("Ramesh K P", 5, 1, 2, 3, 4))
print(destructure_check("Ramesh K P", 4, 1, 3))
print(destructure_check("Ramesh K P", 3, 1, 3, 9, 6, 7, 8, -14))
print()
def product(a, b):
    return a * b

numbers = (3, 5)
print(product(*numbers))
print("#" * 30)

print("#" * 30)
print()



















