# CLASS METHOD
# A class method is bund to the class & receives the class as an implicit first argument.
'''
NOTE : Static method can't access or modify class state & gnerally for utility. 
class Student:
    @classmethod  # decorator
    def collage(cls):
        pass
'''

class Person:
    name = "XYZ"
    # def changeName(obj, name):
    #     self.__class__.name = "ARSHAN"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("ARSHAN")
print(p1.name)
print(Person.name)