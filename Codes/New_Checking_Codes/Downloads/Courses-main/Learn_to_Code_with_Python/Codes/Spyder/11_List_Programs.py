# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:27:25 2021
@author: ramesh.kp
"""

print()
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = 1
print(elements)
def product_of_even_indices(elements):
    for i in range(0, len(elements), 2):
        global product
        product *= elements[i]
        if i == len(elements):
            return product
print(product_of_even_indices(elements))
print("#" * 80)

values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]
def odds_sum(numbers):
    total = 0
    for i in numbers:
        if i % 2:
            total += i
    return total

def greatest_numbers(numbers):
    greatest = numbers[0]
    for i in numbers:
        if i > greatest:
            greatest = i
    return greatest

print(odds_sum(values))
print(odds_sum(other_values))
print(greatest_numbers(values))
print(greatest_numbers(other_values))
print()
