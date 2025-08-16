# TYPES OF FUNCTIONS : 
""" 1} BUILT-IN FUNCTIONS               2} USER DEFINED FUNCTIONS
     - print()
     - len()
     - type()
     - range()
"""

# Q: WAP to print length of a list. (list is the parameter)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
print(len(num))
print(type(num))

# OR

cities = ["delhi", "mp", "mumbai", "goa"]
names = ["zoro", "kira", "shanks", "toji"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(names)

# WAP to print the element of a list in a single line. (list is the parameter)
cities = ["delhi", "mp", "mumbai", "goa"]
names = ["zoro", "kira", "shanks", "toji"]

def print_len(list):
    print(len(list))
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(names)
print_list(cities)

# WAP to find the factorial of n. (n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(9)

# WAP to convetr USD to INR.

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(20)