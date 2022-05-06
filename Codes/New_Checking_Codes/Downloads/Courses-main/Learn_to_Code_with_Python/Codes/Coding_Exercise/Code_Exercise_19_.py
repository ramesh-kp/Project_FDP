# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 23:25:14 2021
@author: ramesh.kp

19.	1.	Define a smallest_number function  that accepts a list of numbers.
		It should return the smallest value in the list.
		EXAMPLES
		--------
		smallest_number([1, 2, 3])     => 1
		smallest_number([3, 2, 1])     => 1
		smallest_number([4, 5, 4])     => 4
		smallest_number([-3, -2, -1])  => -3
	2.	Define a concatenate function that accepts a list of strings. 
		The function should return a concatenated string which consists of all list elements whose length is greater than 2 characters.
		EXAMPLES
		--------
		concatenate(["abc", "def", "ghi"])      => "abcdefghi"
		concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
		concatenate(["ab", "cd", "ef", "gh"])   => ""
	3.	Define a super_sum function that accepts a list of strings.
		The function should sum the index positions of the first occurence of the letter “s” in each word. 
		Not every word is guaranteed to have an “s”.
		Don’t use "sum" as a variable name as it’s a built-in keyword.
		EXAMPLES
		--------
		super_sum([])                                 => 0
		super_sum(["mustache"])                       => 2
		super_sum(["mustache", "greatest"])           => 8
		super_sum(["mustache", "pessimist"])          => 4
		super_sum(["mustache", "greatest", "almost"]) => 12
"""

print()
print("#" * 30)
def smallest_number(number_list):
	return min(number_list)

def concatenate(string_list):
    con = ""
    for i in string_list:
        if len(i) > 2:
            con += i
    return con

def super_sum(string_list):
	sum_pos = 0
	for i in string_list:
		if "s" in i:
			sum_pos += i.index("s")
	return sum_pos
    

print(smallest_number([1, 2, 3]))
print(smallest_number([3, 2, 1]))
print(smallest_number([4, 5, 4]))
print(smallest_number([-3, -2, -1]))
print("#" * 30)
print(concatenate(["abc", "def", "ghi"]))
print(concatenate(["abc", "de", "fgh", "ic"]))
print(concatenate(["ab", "cd", "ef", "gh"]))
print("#" * 30)
print(super_sum([]))
print(super_sum(["mustache"]))
print(super_sum(["mustache", "greatest"]))
print(super_sum(["mustache", "pessimist"]))
print(super_sum(["mustache", "greatest", "almost"]))
print("#" * 30)
print()
