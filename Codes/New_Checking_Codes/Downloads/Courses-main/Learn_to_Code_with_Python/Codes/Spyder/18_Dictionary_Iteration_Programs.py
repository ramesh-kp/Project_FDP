# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:39:32 2021
@author: ramesh.kp
"""

print()
print("#" * 30)
chinese_food = {
    "Sesame Chicken": 9.99,
    "Boneless Spare Ribs": 7.99,
    "Fried Rice": 1.99
    }
print(chinese_food)
for i in chinese_food:
    print(f"The food is {i} and its price is {chinese_food[i]}")
print("#" * 30)

# Item Method
college_courses = {
    "History": "Mr. Washington",
    "Math": "Mr. Newton",
    "Science": "Mr. Einstien"
    }
print(college_courses)
for key, value in college_courses.items():
    print(f"The course {key} is being taught by {value}")
for _, value in college_courses.items():
    print(f"The next professor is {value}")
print("#" * 30)

# Keys and Values Methods
cryptocurrency_prices = {
    "Bitcoin":  400000,
    "Ethereum": 7000,
    "Litecoin": 10
    }
print(cryptocurrency_prices)
print(cryptocurrency_prices.keys())
print(cryptocurrency_prices.values())
for currency in cryptocurrency_prices.keys():
    print(f"The next currency is {currency}")
for price in cryptocurrency_prices.values():
    print(f"The next price is {price}")
print("#" * 30)

# The Sorted Function
salaries = {
    "Exexutive Assisstent": 20,
    "CEO": 100
    }
print(salaries)
print(sorted(salaries))
wheel_count = {
    "truck": 2,
    "car": 4,
    "bus": 8,
    "autorikshaw": 3
    }
print(wheel_count)
for vehicle, count in sorted(wheel_count.items()):
    print(f"The next vehicle is a {vehicle} and it has {count} wheels.")
print("#" * 30)

concert_attendees = [
    {"name": "Taylor", "section": 400, "price paid": 99.99},
    {"name": "Christina", "section": 200, "price paid": 149.99},
    {"name": "Jeremy", "section": 100, "price paid": 0}
    ]
for attendee in concert_attendees:
    for key, value in attendee.items():
        print(f"The {key} is {value}.")
print("#" * 30)

# Keyword Arguements Kwargs
def collect_keyword_arguements(**some_param):
    print(some_param)
    print(type(some_param))
    for key, value in some_param.items():
        print(f"The key is {key} and the value is {value}.")

def args_and_kwargs(a, b, *args, **kwargs):
    dict_total = 0
    for value in kwargs.values():
        dict_total += value

    print(f"The total of your regular arguements a and b is {a + b}.")
    print(f"The total of your args tuple is {sum(args)}.")
    print(f"The total of your kwargs dictionary is {dict_total}.")

collect_keyword_arguements(a = 2, b = 3, c = 4)
args_and_kwargs(1, 2, 3, 4, 5, 6, x = 8, y = 9, z = 10)
print("#" * 30)

def height_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254

print(height_to_meters(5, 11))
stats = {
    "feet": 5,
    "inches": 11
    }
print(height_to_meters(**stats))
print("#" * 30)

# Dictionary Comprehension
languages = ["Python", "Java Script", "Ruby"]
print(languages)
lengths = { i: len(i) for i in languages }
filtered_length = { i: len(i) for i in languages if "t" in i }
print(lengths)
print(filtered_length)
word = "supercalifragilisticexpialidocious"
letter_counts = { i: word.count(i) for i in word if i > "j" }
print(letter_counts)
capitals = {
    "New York": "Albany",
    "California": "Sacramento",
    "Texas": "Austin"
    }
print(capitals)
inverted = { j: i for i, j in capitals.items() }
print(inverted)

print("#" * 30)
print()
