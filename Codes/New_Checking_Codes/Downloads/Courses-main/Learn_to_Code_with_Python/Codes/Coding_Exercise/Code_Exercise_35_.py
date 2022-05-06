# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 23:55:44 2021
@author: ramesh.kp

35.	1.	Define a to_dictionary function that accepts a list of strings. 
		The function should return a dictionary where the keys are the strings and the values are their original index positions in the list.
		EXAMPLES
		--------
		detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
		to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}
	2.	Define a length_counts function that accepts a list of strings. 
		The function should return a dictionary where the keys represent length and the values represent how many strings have that length.
		EXAMPLES
		--------
		sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
		length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
		There is 1 string with 6 letters, 2 strings with 9 letters, 2 strings with 7 letters, and 1 string with 4 letters.
"""

print()
print("#" * 30)

detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]

def to_dictionary(elements):
    results = {}
    for index, elememt in enumerate(elements):
        results[elememt] = index
    return results

def length_counts(elements):
    counts = {}
    for i in elements:
        length = len(i)
        current_count = counts.get(length, 0)
        counts[length] = current_count + 1
    return counts

print(to_dictionary(detectives))
print("#" * 30)
print(length_counts(sa_countries))
print("#" * 30)
print()
