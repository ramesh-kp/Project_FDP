# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:29:11 2021
@author: ramesh.kp
"""

print()
print("#" * 30)

class Pokemon():
    def __init__(self, name, speciality, health = 100):
        self.name = name
        self.speciality = speciality
        self.health = health

    def roar(self):
        print("Raaaarr!")

    def describe(self):
        print(f"I am {self.name}. I am a {self.speciality} Pokemon!")

    def take_damage(self, amount):
        self.health -= amount

squirtle = Pokemon("Squirtle", "Water")
charmander = Pokemon(name = "Charmander", speciality = "Fire", health = 110)
squirtle.roar()
charmander.roar()
squirtle.describe()
charmander.describe()
print(squirtle.health)
squirtle.take_damage(20)
print(squirtle.health)
squirtle.health = 60
print(squirtle.health)
print(charmander.health)
print("#" * 30)

# Protected Attributes and Methods
class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware

    def update_firmware(self):
        print("Reaching out to the server for the next version")
        self._firmware += 1

iphone = SmartPhone()
print(iphone._company)
print(iphone._firmware)

iphone.company = "Samsung"
iphone.firmware = "Nonsense"
print(iphone._company)
print(iphone._firmware)

print(iphone.update_firmware())
print(iphone._firmware)
print("#" * 30)
print("#" * 30)
print()
