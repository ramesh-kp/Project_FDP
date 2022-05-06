# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:57:44 2021
@author: ramesh.kp
"""

import functools

print()
print("#" * 30)
def one():
    return 1

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def calculator(func, a, b):
    return func(a, b)

print(type(one))
print(calculator(add, 3, 5))
print(calculator(substract, 10, 4))
print("#" * 30)

#   Nested Functions
# Gallons to Cups
# 1 Gallon = 4 Quarts
# 1 Quart = 2 Pints
# 1 Pint = 2 Cups    
def convert_gallons_to_cups(gallons):
    def gallons_to_quarts(gallons):
        print(f"Converting {gallons} gallons to quarts !")
        return gallons * 4

    def quarts_to_pints(quarts):
        print(f"Converting {quarts} quarts to pints !")
        return quarts * 2
    def pints_to_cups(pints):
        print(f"Converting {pints} pints to cups !")
        return pints * 2

    quarts = gallons_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    cups = pints_to_cups(pints)
    return cups

print(convert_gallons_to_cups(1))
print(convert_gallons_to_cups(3))
print("#" * 30)

def calculator(operation):
    return_string = "Invalid Operation"
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def invalid(a, b):
        return return_string
    
    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract
    else:
        return invalid

print(calculator("add")(10, 4))
print(calculator("subtract")(7, 7))
print(calculator("multiply")(10, 7))
print("#" * 30)

def square(num):
    return num ** 2
def cube(num):
    return num ** 3
def times10(num):
    return num ** 10

operations = [square, cube, times10]
for func in operations:
    print(func(5))
print("#" * 30)

# Global and Local Variables
age = 28
TAX_RATE = 0.08

def fancy_func():
    age = 100
    print(age)

def calculate_tax(price):
    return round(price * TAX_RATE, 2)

def calculate_tip(price):
    return round(price * (TAX_RATE * 3), 2)

fancy_func()
print(age)
print(calculate_tax(10))
print(calculate_tip(10))
print("#" * 30)

# LEGB Rules - Local / Enclosing Functions / Global / Built in
def outer():
    # Enclosing Funciton Scope
    # x = 10
    def inner():
        # Local Scope
        # x = 5
        return len
    return inner()

print(outer()("Ramesh K P"))
print("#" * 30)

# Closures
def outer():
    candy = "Snickers"
    def inner():
        return candy
    return inner()

the_func = outer()
print(the_func)
print("#" * 30)

# Global Keyword
x = 10
def change_stuff():
    global x
    x = 15
    
print(x)
change_stuff()
print(x)
print("#" * 30)

# The Nonlocal Keyword
def outer():
    bubble_tea_flavor = "Black"
    def inner():
        nonlocal bubble_tea_flavor
        bubble_tea_flavor = "Taro"
    inner()
    return bubble_tea_flavor

print(outer())
print("#" * 30)

# Decorators
# def be_nice(fn):
#     def inner():
#         print("Nice to meet you! I'm honored to execute your function for you!")
#         fn()
#         print("It was my pleasure executing your function! Have a nice day!")
#     return inner

# def complex_bussiness_logic():
#     print("Something Complex!")
    
# result = be_nice(complex_bussiness_logic)
# print(result())
# print("-" * 30)
# be_nice(complex_bussiness_logic)()
# print("-" * 30)

def be_nice(fn):
    def inner():
        print("Nice to meet you! I'm honored to execute your function for you!")
        fn()
        print("It was my pleasure executing your function! Have a nice day!")
    return inner

@be_nice
def complex_bussiness_logic():
    print("Something Complex!")

@be_nice
def another_fancy_function():
    print("Goo goo gaga")

complex_bussiness_logic()
print("-" * 30)
another_fancy_function()
print("#" * 30)

def be_nice(fn):
    def inner(*first, **second):
        print("-" * 30)
        print(first)
        print(second)
        print("-" * 30)
        print("Nice to meet you! I'm honored to execute your function for you!")
        fn(*first, **second)
        print("It was my pleasure executing your function! Have a nice day!")
    return inner
        
@be_nice
def complex_bussiness_logic(stakeholder, position):
    print(f"Something Complex for {position} {stakeholder}")
    
complex_bussiness_logic("Ramesh K P", "Embedded Engineer")
complex_bussiness_logic(stakeholder = "Ramesh K P", position = "Embedded Engineer")
complex_bussiness_logic("Ramesh K P", position = "Embedded Engineer")
print("#" * 30)

def be_nice(fn):
    def inner(*first, **second):
        print("Nice to meet you! I'm honored to execute your function for you!")
        result = fn(*first, **second)
        print(result)
        print("It was my pleasure executing your function! Have a nice day!")
    return inner
        
@be_nice
def complex_bussiness_logic(a, b):
    return a + b

complex_bussiness_logic(5, 3)
print("#" * 30)

def be_nice(fn):
    @functools.wraps(fn)
    def inner(*first, **second):
        print("Nice to meet you! I'm honored to execute your function for you!")
        result = fn(*first, **second)
        print(result)
        print("It was my pleasure executing your function! Have a nice day!")
    return inner
        
@be_nice
def complex_bussiness_logic(a, b):
    "Adds two numbers together"
    return a + b

help(complex_bussiness_logic)
print("#" * 30)
print()
