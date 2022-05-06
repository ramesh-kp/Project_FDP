# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:53:23 2021
@author: ramesh.kp

41.	1.	You are writing a Python program to model a remote control for a television set. 
		Declare a stations_to_numbers function that accepts a dictionary. 
		The keys will be channel numbers and the values will be the station names.
		The stations_to_numbers function should return an inverted dictionary where the keys are the station names and the values are the channel numbers.
		EXAMPLES
		--------
		channels = {2: "CBS", 4: "NBC", 5: "FOX", 7: "ABC"}
		stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}
	2.	Declare a coaster_conversion function that accepts a dictionary.
		The keys of the dictionary will be strings representing roller coasters.
		The values will be the heights of each coaster in meters.
		Return a new dictionary with the same keys.
		The values should be the heights converted from meters to feet.
		The final values (in feet) should also be rounded to the closest integer.
		HINT: 1 meter is equal to 3.28084 feet.
		HINT: The round function rounds a number to the nearest integer.
		EXAMPLES
		--------
		coasters = {"Kingda Ka": 139, "Top Thrill Dragster": 130, "Superman: Escape From Krypton": 126}
		coaster_conversion(coasters) => {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}
"""

print()
print("#" * 30)

channels = {2: "CBS", 4: "NBC", 5: "FOX", 7: "ABC"}
coasters = {"Kingda Ka": 139, "Top Thrill Dragster": 130, "Superman: Escape From Krypton": 126}

def stations_to_numbers(channels):
    return {station: number for number, station in channels.items()}

def coaster_conversion(coasters):
    return {coaster: round(meters * 3.28084) for coaster, meters in coasters.items()}

print(stations_to_numbers(channels))
print("#" * 30)
print(coaster_conversion(coasters))
print("#" * 30)
print()
