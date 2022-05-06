# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:46:24 2021
@author: ramesh.kp
"""

print()
print("#" * 30)
with open("Home_Address.txt", "r") as home_address_file:
    print("The file has been opened")
    content = home_address_file.read()
    print(content)

with open("Office_Address.txt", "r") as office_address_file:
    for line in office_address_file:
        print(line)
print()

print("The file has been closed. We are outside the context block!")
print("#" * 30)
print()
