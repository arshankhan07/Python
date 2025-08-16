#Range function returns a sequence of numbers, starting from 0 by default,
# and increment by 1 (by default), and stops before a specificnumber.
#range(start?, stop, step?)

sequence = range(10)
for i in sequence:
    print(i)

# OR
for i in range(10): #where 10 is range(stop)
    print(i)

for i in range(2, 10): #where 2 is range(start) and 10 is range(stop)
    print(i)

#also printing even numbers:
for i in range(2, 10, 2): #where 2 is range(start) and 10 is range(stop) and again 2 is range(step) means numbers will print in the range of 2 i.e. 2, 4, 6.... 
    print(i)

#also printing odd numbers:
for i in range(1, 10, 2):
    print(i)