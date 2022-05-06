# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:47:17 2021
@author: ramesh.kp


18.	1.	Define a sum_of_lengths function that accepts a list of strings.
		The function should return the sum of the string lengths.
		EXAMPLES
		--------
		sum_of_lengths(["Hello", "Bob"])                  => 8
		sum_of_lengths(["Nonsense"])                      => 8
		sum_of_lengths(["Nonsense", "or", "confidence"])  => 20
	2.	Define a product function that accepts a list of numbers.
		The function should return the product of the numbers.
		The list will always have at least one value.
		EXAMPLES
		--------
		product([1, 2, 3])     => 6
		product([4, 5, 6, 7])  => 840
		product([10])          => 10
"""

print()
print("#" * 30)
def sum_of_lengths(strings):
    return sum(len(i) for i in strings)

def product(number_list):
    # return eval('*'.join(str(i) for i in number_list))
    ######################################################
    product = 1
    for i in range(0, len(number_list)):
        product *= int(number_list[i])
    return product
    
print(sum_of_lengths(["Hello", "Bob"]))
print(sum_of_lengths(["Nonsense"]))
print(sum_of_lengths(["Nonsense", "or", "confidence"]))
print("#" * 30)
print(product([1, 2, 3]))
print(product([4, 5, 6, 7]))
print(product([10]))
print("#" * 30)
print()
