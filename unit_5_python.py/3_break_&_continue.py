#break : used to terminate the loop when encountered.

#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 25
i = 0 
while i < len(num):
    if(num[i] == x):
        print("Found at idx", i)
        break
else:
    print("finding....")
    i += 1
print("end of loop")

#continue : terminates execution in the current 
# and continues execution of the loop with the next iteration.

i = 0
while i <= 10:
    if(i == 3):
        i += 1
        continue
    print(i)
    i =+ 1