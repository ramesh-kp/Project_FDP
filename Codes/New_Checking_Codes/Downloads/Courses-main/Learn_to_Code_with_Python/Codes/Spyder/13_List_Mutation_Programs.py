# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:58:25 2021
@author: ramesh.kp
"""

print()
# Append Function
name = ["Ramesh K P", "Sreejisha P", "Dhruv Srang K P"]
print(name)
name.append("Ramankutty K P")
name.append("Shylaja E")
print(name)
print("#" * 80)

# Extend Function
family = ["Ramesh K P", "Sreejisha P", "Dhruv Srang K P"]
print(family)
family.extend(["Ramankutty K P", "Shylaja E"])
print(family)
print("#" * 80)

# Insert Function
members = ["Ramesh K P", "Sreejisha P", "Dhruv Srang K P"]
print(members)
members.insert(0, "Ramankutty K P")
members.insert(1, "Shylaja E")
print(members)
print("#" * 80)

# Pop Function
group = ["Ramesh K P", "Sreejisha P", "Dhruv Srang K P", "Ramankutty K P", "Shylaja E"]
first_removed = group.pop(-2)
print(group)
print(first_removed)
second_removed = group.pop()
print(group)
print(second_removed)
print("#" * 80)

# Del Function
numbers = ["Zero","One", "Two", "Three", "Four", "Five"]
print(numbers)
del numbers[2:4]
print(numbers)
print("#" * 80)

# Remove Function
numbers = ["Zero","One", "Two", "Three", "Four", "Five"]
print(numbers)
numbers.remove("Three")
print(numbers)
print("#" * 80)

# Clear Function
numbers = ["Zero","One", "Two", "Three", "Four", "Five"]
print(numbers)
numbers.clear()
print(numbers)
print("#" * 80)

# Reverse Function
numbers = ["Zero","One", "Two", "Three", "Four", "Five"]
print(numbers)
numbers.reverse()
print(numbers)
print("#" * 80)

# Sorted Function
numbers = ["Zero","One", "Two", "Three", "Four", "Five"]
digits = [4, 2, 5, 1, 3, 0]
print(numbers)
print(digits)
numbers.sort()
print(numbers)
sorted_digit = sorted(digits)
print(sorted_digit)
print(digits)
digits.sort()
print(digits)
print("#" * 80)
print()
