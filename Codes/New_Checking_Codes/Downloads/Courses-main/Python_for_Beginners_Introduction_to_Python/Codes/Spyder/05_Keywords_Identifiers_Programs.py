# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:40:11 2021
@author: ramesh.kp
"""

import math as MyMath
from math import cos

print("\n")
print(5 == 5)
print(5 > 5)
print("..........")

print(None == 0)
print(None == False)
print(None == [])
print(None == None)
print("..........")

def a_void_function():
    a = 1
    b = 2
    c = a + b
    return c
print(a_void_function())
print("..........")

print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not True)
print(not False)
print("..........")

print(MyMath.cos(MyMath.pi))
print("..........")

assert 5 > 4
assert 5 == 5

for i in range(1, 11):
    if i == 5:
        break
    print(i)
print("..........")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print("..........")

class ExampleClass:
    def function1(parameters):
        print("Function 1 is executing")
    def function2(parameters):
        print("Function 2 is executing")
ob1 = ExampleClass()
ob1.function1()
ob1.function2()
print("..........")

num = 5
if num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
else:
    print("Something Else")
print("..........")

try:
    x = 9
    #raise ZeroDivisionError
except ZeroDivisionError:
    print("Division cannot be performed")
finally:
    print("Execution Successfully")
print("..........")

for i in range(1,100,20):
    print(i)
print("..........")

print(cos(30))
print("..........")

globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15
read1()
write1()
read1()
write2()
read1()
print("..........")

a = [1, 2, 3, 4]
print(4 not in a)
print(44 not in a)
print(4 in a)
print(44 in a)
print("..........")

print(5 is 5)
print("..........")

a = lambda x: x*2
for i in range(1, 6):
    print(i, a(i))
print("..........")

def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("inner function ", a)
    inner_function()
    print("outer function ", a)
outer_function()
print("..........")

def function(parameters):
    pass
function(10)
print("..........")

def fun_return():
    a = 10
    return a
print(fun_return())
print("..........")    

i = 5
while i > 0:
    print(i)
    i -= 1
print("..........")

with open("text.txt", "w") as my_file:
    my_file.write("Ramesh K P \n Kizhakkepurath House \n Amminikkad P O")   
print("..........")

def generator():
    for i in range(11):
        yield i*i*i
g = generator()
for i in g:
    print(i)
print("..........")

print("\n")
