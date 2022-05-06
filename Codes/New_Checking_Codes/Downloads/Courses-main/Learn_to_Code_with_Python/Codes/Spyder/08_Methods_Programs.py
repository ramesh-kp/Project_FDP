# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 09:24:16 2021
@author: ramesh.kp
"""

#
print()
browser = "Google Chrome"
print(browser.find("C"))
print("#" * 80)

salutations = "Mr. Kermit the Frog"
print(salutations.startswith("Mr."))
print(salutations.endswith("Frog"))
print(salutations.endswith("frog"))
print("#" * 80)

word = "queueing"
print(word.count("ue"))
print("#" * 80)

def find_my_letter(word, character):
    return word.find(character)
a = find_my_letter("Ramesh", "m")
print(a)
print("#" * 80)

story = "once upon a time"
name = "RAMESH"
origin = "Ramesh K P"
print(story.capitalize())
print(story.title())
print(story.upper())
print(name.lower())
print(origin.swapcase())
print(story.lower().title())
print("#" * 80)

print("winter".islower())
print("SUMMER".isupper())
print("The Four Seasons".istitle())
print("Area".isalpha())
print("123456789".isnumeric())
print("Area51".isalnum())
print("  ".isspace())
print("#" * 80)

name = "          Ramesh K P          "
print(len(name))
print(name.rstrip())
print(len(name.rstrip()))
print(name.lstrip())
print(len(name.lstrip()))
print(name.strip())
print(len(name.strip()))
website = "www.facebook.com"
print(website.rstrip(".com"))
print(website.lstrip("w."))
print(website.strip("w.com"))
print("#" * 80)

phone_number = "04933 226859"
print(phone_number.replace(" ", "-"))
print("#" * 80)

name = "Bobby"
adjective = "Green"
noun = "Alien"
mad_libs = "{} laughed at the {} {}." 
print(mad_libs.format(name, adjective, noun))
mad_libs = f"{name} laughed at the {adjective} {noun}." 
print(mad_libs)
print()
