# Q: Create student class that takes name and marks of 3 subjects as arguments in constructor.
# then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is : ", sum/3)
s1 = Student("arshan", [99, 96, 95])
s1.get_avg()