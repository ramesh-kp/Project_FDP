# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:50:35 2021
@author: ramesh.kp
"""

print("\n")
first_tuple = ()
print(first_tuple)
sec_tuple = (1, 2, 3)
print(sec_tuple)
third_tuple = (101, "Ramesh K P", 60000.00, "Embedded Department")
print(third_tuple)
fourth_tuple = ("Points", [1, 4, 3], (7, 8, 6))
print(fourth_tuple)
print("..........")

fifth_tuple = 101, "Ramesh K P", 60000.00, "Embedded Department"
print(fifth_tuple)
empid, empname, empsal, empdep = fifth_tuple
print(empid)
print(empname)
print(empsal)
print(empdep)
print("..........")

sixth_tuple = ("w", "e", "l", "c", "o", "m", "e")
print(sixth_tuple)
print(sixth_tuple[1])
print(sixth_tuple[3])
print(sixth_tuple[5])
print("..........")

sev_tuple = ("Point", [1, 3, 4], (8, 7, 9))
print(sev_tuple)
print(sev_tuple[0][3])
print(sev_tuple[1][2])
print(sev_tuple[2][2])
print("..........")

eigh_tuple = ("w", "e", "l", "c", "o", "m", "e")
print(eigh_tuple)
print(eigh_tuple[1:3])
print(eigh_tuple[:-3])
print(eigh_tuple[3:])
print(eigh_tuple[:])
print("..........")

nin_tuple = ("w", "e", "l", "c", "o", "m", "e")
print(nin_tuple)
nin_tuple = ("G", "O", "O", "D", "B", "Y", "E")
print(nin_tuple)
print("..........")

ten_tuple1 = ("w", "e", "l")
ten_tuple2 = ("c", "o", "m", "e")
print(ten_tuple1 + ten_tuple2)
print(("again", )*4)
print("..........")

ele_tuple = ("R", "a", "m", "e", "s", "h", " ", "K", " ", "P")
print(ele_tuple)
print(ele_tuple.count("e"))
print(ele_tuple.index("K"))
print("c" in ele_tuple)
print("a" in ele_tuple)
for i in ele_tuple:
    print("Letters are -> ", i)
print("..........")

twe_tuple = (22, 33, 55, 44, 77, 66, 11)
print(twe_tuple)
print(max(twe_tuple))
print(min(twe_tuple))
print(sorted(twe_tuple))
print(len(twe_tuple))
print("..........")
