# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:32:31 2021
@author: ramesh.kp
"""

print()
print("#" * 30)

numbers = [4, 8, 15, 16, 23, 42]
animals = ["cat", "bear", "Zebra", "donkey", "cheetah"]
metals = ["gold", "silver", "platinum", "palladium"]

# Map Functions
def cubes(number):
    return number ** 3

print(list(map(cubes, numbers)))
print(list(map(len, animals)))
print("#" * 30)

# Filter Functions
def is_long_animal(animal):
    return len(animal) > 5
print(animals)
print(list(filter(is_long_animal, animals)))
print("#" * 30)

# Lambda Functions
print(list(filter(lambda i: len(i) > 5, metals)))
print(list(filter(lambda i: "p" in i, metals)))
print(list(map(lambda i: i.count("l"), metals)))
print(list(map(lambda i: i.replace("s", "$"), metals)))
print("#" * 30)

# All and Any Functions
print(all([]))
print(all([True]))
print(all([True, True, False]))
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all(["a", "b"]))
print(all(["a", "b", ""]))
print()
print(any([]))
print(any([True]))
print(any([True, True, False]))
print(any([1, 2, 3]))
print(any([1, 2, 3, 0]))
print(any(["a", "b"]))
print(any(["a", "b", ""]))
print("#" * 30)

# Max and Min Functions
print(max([3, 5, 7]))
print(min([3, 5, 7]))
print(max(["D", "G", "Z"]))
print(min(["D", "G", "Z"]))
print("#" * 30)

# Sum and Dir Function
print(sum([2, 3, 4]))
print(sum([1.2, 2.4, 3.6]))
print(dir(int))
print(dir(str))
print("#" * 30)

# Format Function
number = 0.123456789
print(format(number, "f"))
print(format(number, ".2f"))
print(format(0.5, ".2%"))
print(format(123456789, ","))
print("#" * 30)
print()
