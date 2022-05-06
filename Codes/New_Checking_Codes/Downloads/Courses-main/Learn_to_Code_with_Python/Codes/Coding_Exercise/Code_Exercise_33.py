# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 18:25:31 2021
@author: ramesh.kp

33.	a.	Given the tuple below, destructure the three values and assign them to position, city and salary variables
		Do not use index positions (i.e. job_opening[1])
		--------
		job_opening = ("Software Engineer", "New York City", 100000)
	b.	Given the tuple below, 
		- destructure the first value and assign it to a street variable.
		- destructure the last value and assign it to a zip_code variable.
		- destructure the middle two values into a list and assign it to a city_and_state variable.
		--------
		address = ("35 Elm Street", "San Francisco", "CA", "94107")
	c.	Declare a sum_of_evens_and_odds function that accepts a tuple of numbers.
		It should return a tuple with two numeric values:
		-- the sum of the even numbers
		-- the sum of the odd numbers.
		EXAMPLES
		--------
		sum_of_evens_and_odds((1, 2, 3, 4))   => (6, 4)
		sum_of_evens_and_odds((1, 3, 5))      => (0, 9)
		sum_of_evens_and_odds((2, 4, 6))      => (12, 0)
"""

print()
print("#" * 30)
job_opening = ("Software Engineer", "New York City", 100000)
position, city, salary = job_opening
print(position, city, salary, sep = "__")
print("#" * 30)

address = ("35 Elm Street", "San Francisco", "CA", "94107")
street, *city_and_state, zip_code = address
print(street, *city_and_state, zip_code, sep = "__")
print("#" * 30)

def sum_of_evens_and_odds(number_tuple):
    # even_numbers = [i for i in number_tuple if not i % 2]
    # odd_numbers = [i for i in number_tuple if i % 2]
    # return sum(even_numbers), sum(odd_numbers)
	return sum([i for i in number_tuple if not i % 2]), sum([i for i in number_tuple if i % 2])

print(sum_of_evens_and_odds((1, 2, 3, 4)))
print(sum_of_evens_and_odds((1, 3, 5)))
print(sum_of_evens_and_odds((2, 4, 6)))
print("#" * 30)
print()
