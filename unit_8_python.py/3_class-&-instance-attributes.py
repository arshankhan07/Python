# CLASS & INSTANCE ATTRIBUTES
'''
class.attr
obj.attr
'''
# METHODS 
# methods are function that belongs to object.

# CREATE CLASS 
'''
class Student:
    def __init__(self, fullname):
        self,name = fllname

def hello(self):
    print("hello", self.name)
'''

# CREATING OBJECTk
'''
s1 = Student("Arshan")
s1.hello
'''

class Student:
    collage_name = "XYZ"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Arshan", 97)
s1.welcome()
print(s1.get_marks())
s2 = Student("xyz", 96)
s2.welcome()
print(s2.get_marks())