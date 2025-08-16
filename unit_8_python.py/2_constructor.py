# _ _init_ _ {constructor} function
#All classes have a function called _ _init_ _(), which is always executed when the object is being initiated.
# the data/variables that is stored inside the class or object is known as attributes.
# CREATING CLASS 
'''
class student:
    def _ _init_ _(self, fullname):
        self.name = fullname
'''
# CREATING OBJECT
'''
s1 = Student("Arshan")
print(s1.name)
'''
# the SELF parameter id a reference to yhe current instance of the class, and is used to access varivbles that belongs to the class.
'''
class Student:
    name = "Arshan"
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in database..")

s1 = Student("Arshan")
print(s1.name)

s2 = Student("xyz")
print(s2.name)
'''

class Student:
# default constructor -> always ctreated default by python i.e. if we dont write it python will apply it bydefault without any error.
    def __init__(self):
        pass
    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("Arshan", 97)
print(s1.name, s1.marks)

s2 = Student("xyz", 96)
print(s2.name, s2.marks)