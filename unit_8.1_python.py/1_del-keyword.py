# DEL KEYWORD 
# Used to delete object properties or object itself.
'''
del s1.name
del s1
'''

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Arshan")

del s1
print(s1) #o/p : error