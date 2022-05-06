# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:54:37 2021
@author: ramesh.kp

29.	1.	Uncomment the commented lines of code below and complete the list comprehension logic.
		a.	The floats variable should store the floating point values for each string in the values list.
			--------
			values = ["3.14", "9.99", "567.324", "5.678"]
			# floats = []
		b.	The letters variable should store a list of 5 strings. 
			Each of the strings should be a character from name concatenated together 3 times.
			i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
			--------
			name = "Boris"
			# letters = []
		c.	The 'lengths' list should store a list with the lengths of each string in the 'elements' list.
			--------
			elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
			# lengths = []
	2.	Declare a destroy_elements function that accepts two lists.
		It should return a list of all elements from the first list that are NOT contained in the second list.
		Use list comprehension in your solution.
		EXAMPLES
		--------
		destroy_elements([1, 2, 3], [1, 2])      => [3]
		destroy_elements([1, 2, 3], [1, 2, 3])   => []
		destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]
"""

print()
print("#" * 30)
values = ["3.14", "9.99", "567.324", "5.678"]
print(values)
floats = [float(i) for i in values]
print(values)
print("#" * 30)

name = "Ramesh"
print(name)
letters = [i * 3 for i in name]
print(letters)
print("#" * 30)

elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
print(elements)
lengths = [len(i) for i in elements]
print(lengths)
print("#" * 30)

def destroy_elements(first, second):
    return [i for i in first if i not in second]

print(destroy_elements([1, 2, 3], [1, 2]))
print(destroy_elements([1, 2, 3], [1, 2, 3]))
print(destroy_elements([1, 2, 3], [4, 5]))
print("#" * 30)
print()
