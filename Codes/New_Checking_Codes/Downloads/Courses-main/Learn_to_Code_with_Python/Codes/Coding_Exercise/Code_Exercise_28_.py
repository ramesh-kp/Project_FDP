# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:43:18 2021
@author: ramesh.kp

28.	1.	Define a nested_sum function that accepts a list of lists of numbers.
		The function should return the sum of the values.
		The list may contain empty lists.
		EXAMPLES
		--------
		nested_sum([[1, 2, 3], [4, 5]])            => 15
		nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
		nested_sum([[]])                           => 0
	2.	Define a fancy_concatenate function that accepts a list of lists of strings.
		The function should return a concatenated string.
		The strings in a list should only be concatenated if the length of the list is 3.
		EXAMPLES
		--------
		fancy_concatenate([["A", "B", "C"]])                        => "ABC"
		fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
		fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
		fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
		fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""
"""

print()
print("#" * 30)
def nested_sum(number_list):
    total = 0
    for row in number_list:
        for value in row:
            total += value
    return total

def fancy_concatenate(string_list):
    final = ""
    for row in string_list:
        if len(row) == 3:
            for value in row:
                final += value
    return final

print(nested_sum([[1, 2, 3], [4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))
print("#" * 30)
print(fancy_concatenate([["A", "B", "C"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))
print(fancy_concatenate([["A", "B"], ["C", "D"]]))
print("#" * 30)
print()
