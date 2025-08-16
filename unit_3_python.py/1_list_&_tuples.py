#list
#list is a built in data type that stores set of values in a particular order.
#it can store elements of different data types.{int,float,string,boolean,etc.}
#EG: student = ["arshan, 19, jabalpur, collage"]

student = ["arshan, 19, jabalpur, collage"]
print(student)

# to change any value in the list.
student = ["arshan", 19, "jabalpur", "collage"]
student[0] = "ARSHAN"
print(student)

#list is a collection of items in a particular order.
#list is a mutable data type.
#list is defined using square brackets.
#list is a sequence type.
#list is a heterogeneous data type.
#list is a dynamic data type
# #starts from 0 index to n-1 index.

marks1 = 94.4
marks2 = 95.5
marks3 = 96.6
marks4 = 97.7
marks5 = 98.8

marks = [94.4, 95.5, 96.6, 97.7, 98.8]

print(marks)
print(type(marks))

#to print the perticular element of the list.

marks = [94.4, 95.5, 96.6, 97.7, 98.8]

print(marks[0])
print(marks[1])
print(marks[4])