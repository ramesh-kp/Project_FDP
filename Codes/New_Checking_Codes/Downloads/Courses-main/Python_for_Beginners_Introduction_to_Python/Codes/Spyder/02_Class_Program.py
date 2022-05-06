# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 20:42:05 2021
@author: ramesh.kp
"""

print("\n")
class MyComplexNumber:
    def __init__(self, real = 0, img = 0):
        print("My Complex Number Executing.....")
        self.real_part = real
        self.imag_part = img
        
    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part, self.imag_part))
 
cmplx1 = MyComplexNumber(40, 50)
cmplx1.displayComplex()

cmplx2 = MyComplexNumber(60, 70)
cmplx2.new_attribute = 80
cmplx2.displayComplex()
print(cmplx2.real_part, cmplx2.imag_part, cmplx2.new_attribute)

del cmplx1.real_part
print(cmplx1)

#del cmplx1
#print(cmplx1)

print(("\n"))
