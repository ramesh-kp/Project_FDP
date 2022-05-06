# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 16:50:54 2021
@author: ramesh.kp
"""

print("\n")
first_set = {11, 33, 66, 55, 44, 22}
print(first_set)
second_set = {101, "Ramesh", (21, 2, 1989)}
print(second_set)
print("..........")

third_set = set([1, 2, 3, 2])
print(third_set)
first_list = set({1, 2, 3, 2})
print(first_list)
print("..........")

print(first_set)
first_set.add(77)
print(first_set)
first_set.update([88, 99, 111])
print(first_set)
first_set.update([101, 102], {104, 103, 105})
print(first_set)
print("..........")

first_set.discard(101)
print(first_set)
first_set.remove(102)
print(first_set)
print(third_set)
print(third_set.pop())
print(third_set)
third_set.clear()
print(third_set)
print("..........")

fourth_set = {0, 1, 2, 3, 4, 5}
fifth_set = {4, 5, 6, 7, 8, 9}
print(fourth_set)
print(fifth_set)
print(fourth_set | fifth_set)
print(fourth_set.union(fifth_set))
print(fourth_set & fifth_set)
print(fourth_set.intersection(fifth_set))
print(fourth_set - fifth_set)
print(fourth_set.difference(fifth_set))
print(fifth_set - fourth_set)
print(fifth_set.difference(fourth_set))
print(fourth_set ^ fifth_set)
print(fourth_set.symmetric_difference(fifth_set))
print("..........")

print(first_set)
print(66 in first_set)
print(66 not in first_set)
print("..........")

for i in set("Ramesh"):
    print(i)
print("..........")

print(first_set)
print(len(first_set))
print(max(first_set))
print(min(first_set))
print(sorted(first_set))
print("..........")

fourth_set = frozenset(fourth_set)
fifth_set = frozenset(fifth_set)
print(fourth_set)
print(fifth_set)
print(fourth_set.difference(fifth_set))
print(fourth_set.union(fifth_set))
print(fourth_set.intersection(fifth_set))
print(fourth_set.symmetric_difference(fifth_set))
print("\n")
