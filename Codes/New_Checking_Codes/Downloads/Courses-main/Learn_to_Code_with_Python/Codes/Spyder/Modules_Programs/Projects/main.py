# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:51:10 2021
@author: ramesh.kp
"""

# import Feature.Copyright

# print(Feature.Copyright.date_of_copyright)

import Feature.Subfeature.Calculator
import Feature.Copyright
from Feature.Subfeature import Calculator
#from Feature.Subfeature.Calculator import substract
import Feature.Subfeature

print(Feature.Subfeature.Calculator.substract(10, 5))
print(Feature.Copyright.date_of_copyright)
print(Calculator.substract(10, 3))
#print(substract(10, 3))
print(Feature.Subfeature.substract(10, -1))
