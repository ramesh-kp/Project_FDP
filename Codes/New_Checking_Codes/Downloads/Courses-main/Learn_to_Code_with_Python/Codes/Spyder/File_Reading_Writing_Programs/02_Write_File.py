# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 15:22:26 2021
@author: ramesh.kp
"""

print()
print("#" * 30)

file_name = "Written_Files.txt"
with open(file_name, "w") as write_files:
    write_files.write("Hello File \n")
    write_files.write("You are my first written file")

with open(file_name, "a") as append_file:
    append_file.write("\nAppended line to the existing file")

print("#" * 30)
print()
