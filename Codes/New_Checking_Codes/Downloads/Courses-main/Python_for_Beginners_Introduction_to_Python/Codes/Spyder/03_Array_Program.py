# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:34:12 2021
@author: ramesh.kp
"""

print("\n")
arr = [10, 20, 30, 40, 50]
print(arr)

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-2])
print(arr[-1])

brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print(brands)
num_brands = len(brands)
print(num_brands)
brands.append("Intel")
print(brands)

colors_one = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
print(colors_one)
del colors_one[4]
print(colors_one)
colors_one.remove("blue")
print(colors_one)
colors_one.pop(3)
print(colors_one)

fruits_one = ["apple", "banana", "mango", "grapes", "orange"]
print(fruits_one)
fruits_one[1] = "pineapple"
print(fruits_one)
fruits_one[-1] = "guava"
print(fruits_one)

concat = [1, 2, 3]
concat = concat + [4, 5, 6]
print(concat)

repeat = "a"
print(repeat)
repeat = repeat * 5
print(repeat)

fruits_two = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits_two)
print(fruits_two[1:4])
print(fruits_two[:3])
print(fruits_two[-4:])
print(fruits_two[-3:-1])

multd = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])

print("\n")
