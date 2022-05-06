# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 21:47:25 2021
@author: ramesh.kp
"""

print("")
print("Simple Calculator")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. %")
first_number = int(input("Enter the first digit: "))
second_number = int(input("Enter the second digit: "))
operator = input("Enter the arithmatic operation: ")

def simple_calculator(first_number, second_number, operator):
    if operator == "1" or operator == "+":
        return first_number + second_number
    elif operator == "2" or operator == "-":
        return first_number - second_number
    elif operator == "3" or operator == "*":
        return first_number * second_number
    elif operator == "4" or operator == "/":
        return first_number / second_number
    elif operator == "5" or operator == "%":
        return first_number % second_number
    else:
        return "Unknown Input"

print()
print(simple_calculator(first_number, second_number, operator))
