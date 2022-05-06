# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 06:11:37 2021
@author: ramesh.kp
"""

print()
print("#" * 30)

# class Guitar():
#     def __init__(self):
#         print(f"A new guitar is being created! This object is {self}")
class Guitar():
    def __init__(self, wood):
        self.wood = wood

# acoustic = Guitar()
# electric = Guitar()
print("#" * 30)

# acoustic.wood = "Mahogany"
# acoustic.strings = 6
# acoustic.year = 1990
# electric.nickname = "Sound Viking 3000"
# print(acoustic.wood)
# print(acoustic.strings)
# print(acoustic.year)
# print(electric.nickname)
print("#" * 30)

acoustic = Guitar("Alder")
elctric = Guitar("Mahogany")
baritone = Guitar("Alder")
print(acoustic.wood)
print(elctric.wood)
print(baritone.wood)
print("#" * 30)

class Book():
    def __init__(self, title, author, price = 14.99):
        self.title = title
        self.author = author
        self.price = price

animal_farm = Book("Animal Farm", "George Orwell", "19.99")
gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
atlas = Book(title = "Atlas Shrugged", author = "Ayn Rand")
jude = Book(author = "Thomas Hardy", price = 24.99, title = "Jude the Obscure")
print(animal_farm.price)
print(gatsby.price)
print(jude.title)
print("#" * 30)
print()
