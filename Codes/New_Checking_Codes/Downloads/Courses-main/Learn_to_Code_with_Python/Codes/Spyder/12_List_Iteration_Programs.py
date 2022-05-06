# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 22:09:45 2021
@author: ramesh.kp
"""

print()
# Reversed Functions
the_simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
for i in reversed(the_simpsons):
    print(i)
    print(f"{i} has a total of {len(i)} characters.")
print("#" * 80) 

# Enumerate Functions
errand = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]
for index, elements in enumerate(errand, 1):
    print(index, elements)
    print(f"{elements} is number {index} on my list of things to do today!")
print("#" * 80) 

# Range Functions
for i in range(99, -1, -11):
    print(i)
print("#" * 80)

# Command line arguements
# Run the file with "run Python_File.py" with "Input_Data"
import sys
word_lengths = 0
for arg in sys.argv[1:]:
    word_lengths += len(arg)
print(word_lengths)    
print(f"The total length of all command line arguement is {word_lengths}")
print("#" * 80)
print()
