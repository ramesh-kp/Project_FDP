# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:31:15 2021
@author: ramesh.kp

27.	1.	Define a word_lengths function that accepts a string. 
		It should return a list with the lengths of each word.
		EXAMPLES
		--------
		word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
		word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]
	2.	Define a cleanup function that accepts a list of strings.
		The function should return the strings joined together by a space.
		There's one BIG problem -- some of the strings are empty or only consist of spaces!
		These should NOT be included in the final string.
		EXAMPLES
		--------
		cleanup(["cat", "er", "pillar"])           => "cat er pillar"
		cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
		cleanup(["", "", " "])                     => ""
"""

print()
print("#" * 30)
def word_lengths(string):
    # words = string.split(" ")
    # lengths = []
    # for i in words:
    #     lengths.append(len(i))
    # return lengths
	return [len(i) for i in string.split(" ")]

def cleanup(string_list):
    # clean = []
    # for i in string_list:
    #     if i.isspace() or len(i) == 0:
    #         continue
    #     clean.append(i)
    # return " ".join(clean)
	return " ".join(string_list).remove(" ").remove("")

print(word_lengths("Mary Poppins was a nanny"))
print(word_lengths("Somebody stole my donut"))
print("#" * 30)
print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]))
print("#" * 30)
print()
