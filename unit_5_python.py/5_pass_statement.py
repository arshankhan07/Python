#Pass is a null statement that does nothing. it is used as a placeholder for future code.

for i in range(10):
    pass
print("continue")

# Q: WAP to find the sum of first n numbers. (using while)
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum =", sum)


# Q: WRA to find the factorial of first n numbers. (using for)
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)

n = 5
fact = 1
i = 1
for i in range(1, n+1):
    fact *= i
print("factorial =", fact)
