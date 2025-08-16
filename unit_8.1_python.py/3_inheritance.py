# INHERITNCE 
# When one class(child/driver) drives the properties & methods of another class (parent/base).
'''
# Eg of single Inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped....")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name 

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car1.color)
'''

# TYPES OF INHERITANCE 
'''
1) Single Inheritance
2) Multi-level Inheritance
3) Multiple Inheritance
'''

# Multi-level Inheritance
'''
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped....")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.name = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()
'''

# Multiple Inheritance

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)