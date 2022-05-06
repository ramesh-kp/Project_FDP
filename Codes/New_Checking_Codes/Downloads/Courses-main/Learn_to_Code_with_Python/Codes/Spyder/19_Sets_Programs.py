# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:19:50 2021
@author: ramesh.kp
"""

print()
print("#" * 30)
stocks = {"MSFT", "FB", "IBM", "FB"}
print(stocks)
squares = {i **2 for i in [-5, -4, -3, 3, 4, 5]}
print(squares)
print("#" * 30)

# Add and Update Method
disney_characters = {
    "Mickey Mouse",
    "Minnie Mouse",
    "Elsa"
    }
print(disney_characters)
disney_characters.add("Ariel")
disney_characters.update(["Donal Duck", "Goofy"])
disney_characters.update(("Simba", "Pluto", "Mickey Mouse"))
print(disney_characters)
print("#" * 30)

# Remove and Discard Methods
agents = {"Mulder", "Scully", "Doggett", "Reyes"}
print(agents)
agents.remove("Scully")
#agents.remove("Skinner")       Error will occur
agents.discard("Mulder")
agents.discard("Skinner")
print(agents)

# Intersection, Union, Difference and Symmetric Disfference Methods
candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reeses Pieces", "Snickers"}
# Intersection
print(candy_bars.intersection(sweet_things))
print(sweet_things.intersection(candy_bars))
print(candy_bars & sweet_things)
# Union
print(candy_bars.union(sweet_things))
print(sweet_things.union(candy_bars))
print(candy_bars | sweet_things)
# Difference
print(candy_bars.difference(sweet_things))
print(candy_bars - sweet_things)
print(sweet_things.difference(candy_bars))
print(sweet_things - candy_bars)
# Symmetric Difference
print(candy_bars.symmetric_difference(sweet_things))
print(sweet_things.symmetric_difference(candy_bars))
print(candy_bars ^ sweet_things)
print("#" * 30)

# issubset and issuperset Method
a = {1, 2, 4}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))
print(a < b)
print(a <= b)
print(b.issubset(a))
print(b.issuperset(a))
print(b > a)
print(b >= a)
print(a.issuperset(b))
print("#" * 30)

# Frozenset Method
mr_freeze = frozenset([1, 2, 3, 2])
print(mr_freeze)
print({mr_freeze: "Some Value"})
print("#" * 30)
print()
