# FUNCTIONS IN PYTHON 
#block of statement that performs a specific task.
# to create function: 
# def func_name(para1, para2, ..):
#to call function:
#func_name(para1, para2, ..):

def calc_sum(a, b): #function defination ; a & b are parameters
    sum = a + b
    print(sum)
    return sum
calc_sum(5, 22) # function call; 5 & 22 is arguments

def print_hello():
    print("hello")
print_hello()
print_hello()
print_hello()
print_hello()

#average of 3 numbers

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg

calc_avg(41, 52, 84)