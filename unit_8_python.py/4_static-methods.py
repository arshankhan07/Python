# STATIC METHODS
# Method that don't use the self parameter (work at class level)

'''
class Student:
    @staticmethod  #decorator
    def college():
        print("XYZ College")
'''
# Decorator : allows us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
# Q: Create student class that takes name and marks of 3 subjects as arguments in constructor.
# then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is : ", sum/3)
s1 = Student("arshan", [99, 96, 95])
s1.get_avg()
s1.hello()