# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:32:28 2021
@author: ramesh.kp
"""

print()
pizzas = [
    "Mushroom",
    "Pepperoni",
    "Sausage",
    "Barbecue Chicken",
    "Pepperoni",
    "Sausage"
    ]
print(pizzas)

# Count Function
print(pizzas.count("Sausage"))
print(pizzas.count("sausage"))
print("#" * 80)

# Index Function
print(pizzas.index("Sausage"))
print(pizzas.index("Sausage", 2))
print(pizzas.index("Sausage", 3))
print("#" * 80)

# Copy Function
more_pizza = pizzas.copy()
copy_pizza = pizzas[:]
print(pizzas)
print(more_pizza)
print(copy_pizza)
print("#" * 80)

# Split Function
sentence = "I am learning how to code"
print(sentence)
print(sentence.split(" "))
print(sentence.split(" ", 3))
print("#" * 80)

# Join Function
Address = [
    "Kizhakkepurath House",
    "Amminikkad P O",
    "Panambi",
    "Perinthalmanna",
    "Malappuram DST",
    "Pin - 679322"
    ]
print(Address)
print(", ".join(Address))
print("#" * 80)

breakfasts = ["Eggs", "Cereal", "Banana"]
lunches = ["Sushi", "Chicken Teriyaki", "Soup"]
dinners = ["Steak", "Meatballs", "Pasta"]
print(list(zip(breakfasts, lunches, dinners)))
for breakfasts, lunches, dinners in zip(breakfasts, lunches, dinners):
    print(f"My meal for today was {breakfasts} and {lunches} and {dinners}.")
print("#" * 80)

# List Comprehensions
numbers = [3, 4, 5, 6, 7]
squares_first = []
for i in numbers:
    squares_first.append(i ** 2)
print(squares_first)
squares_second = [i **2 for i in numbers]
print(squares_second)
rivers = ["Amazon", "Nile", "Yangtze"]
print([len(i) for i in rivers])
print("#" * 80)

print(["abcdefghijklmnopqrstuvwxyz ".index(i)+1 for i in 
       "abcdefghijklmnopqrstuvwxyz "])
donuts = [
    "Boston Cream",
    "Jelly",
    "Vanilla Cream",
    "Glazed",
    "Chocolate Cream"
    ]
print(donuts)
creamy_donuts = []
for i in donuts:
    if "Cream" in i:
        creamy_donuts.append(i)
print(creamy_donuts)
print([i for i in donuts if "Cream" in i])
print([len(i) for i in donuts if "Cream" in i])
print([i.split(" ")[0] for i in donuts if "Cream" in i])
print("#" * 80)
print()
