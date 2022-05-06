# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:41:51 2021
@author: ramesh.kp

39.	Assign a list of four dictionaries to a "complexity" variable below:
	-	The first and third dictionaries should have two key-value pairs. 
		For those dictionaries, the keys should be strings and the values should be Booleans.
	-	The second and fourth dictionaries should have three key-value pairs.
		For those dictionaries, the keys shoulds be floats and the values should be list of strings. 
		The lists can be of any length.
"""


print()
print("#" * 30)
complexity = [
        {
            "A": True, "B": False
        }, 
        {
            3.4: ["Apple", "Orange"],
            5.7: "Watermelon",
            10.2: ["Grape", "Tangerine", "Mango"]
        },
        {
            "C": True,
            "D": False
        },
        {
            3.4: ["Apple", "Orange"],
            5.7: "Watermelon",
            10.2: ["Grape", "Tangerine", "Mango"]
        }
    ]
print(complexity)
print("#" * 30)
print()
