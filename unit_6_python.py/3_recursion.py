# when a function calls itself repeatedly.

#recursie function #BASE CASE
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(7)
show(5)


#

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(9))
print(fact(4))

# Q: Write a recursive function to calculate the sum of first n naturl numbers.
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(5)
print(sum)

# Q: write a recursive function to print all elements in a list
# hint : use list and index as parameters.
def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "banana", "apple"]
print_list(fruits)