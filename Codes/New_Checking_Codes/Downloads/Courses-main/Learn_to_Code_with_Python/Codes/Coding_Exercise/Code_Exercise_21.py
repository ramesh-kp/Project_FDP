# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:57:06 2021
@author: ramesh.kp

21.	a.	Given the great_directors list below, overwrite the “Steven Spielberg” string with a string of “Michael Bay”.
		--------
		great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]
	b.	Given the transformers list below, overwrite “Bumblebee” with “Grimlock”.
		--------
		transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]
	c.	Given the camping_trip_supplies list below, overwrite "Socks" with "Food".
		--------
		camping_trip_supplies = ["Socks", "Flashlight", "Tent", "Blanket"]
	d.	Given the tech_companies list below, overwrite the Microsoft, Blueberry, and IBM strings with the strings “Facebook” and “Apple”. 
		Use list slicing syntax.
		--------
		tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]
"""

print()
print("#" * 30)

great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]
transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]
camping_trip_supplies = ["Socks", "Flashlight", "Tent", "Blanket"]
tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]

print(great_directors)
great_directors[1] = "Michael Bay"
print(great_directors)
print("#" * 30)
print(transformers)
transformers[2] = "Grimlock"
print(transformers)
print("#" * 30)
print(camping_trip_supplies)
camping_trip_supplies[0] = "Food"
print(camping_trip_supplies)
print("#" * 30)
print(tech_companies)
tech_companies[1:-1] = ["Facebook", "Apple"]
print(tech_companies)
print("#" * 30)
print()
