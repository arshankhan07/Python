#loops are used to repeat instructions.
"""Two types of loops : 
1) While loops
2) For loops"""

#WHILE LOOP CONDITION :

count = 1
while count <= 5:
    print("hello")
    count += 1
    
i = 1
while i <= 5:
    print("arshan", i)
    i += 1

i = 1
while i <= 100:
    print("arshan", i)
    i += 1

#TO print numbers from 1 to 10

i = 1
while i <= 10:
    print(i)
    i += 1

#to print numbers in reverse 
i = 10
while i >= 1:
    print(i)
    i -= 1

#print the multiplication table of a number n.
i = 1
while i <= 10:
    print(3*i)
    i += 1

#print the multiplication table of a number n : user input
n = int(input("enter the number : "))
i = 1
while i <= 10:
    print(n*i)
    i += 1

#print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1

#search for a number x in this tuple using loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 25
i = 0 
while i < len(num):
    if(num[i] == x):
        print("Found at idx", i)
    i += 1