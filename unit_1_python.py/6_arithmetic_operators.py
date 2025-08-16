#arithmetic operators
#+,-,*,/,%,//,**
a = 10
b = 20
print(a + b) #sum
print(a - b) #difference
print(a * b) #product
print(a / b) #division
print(a % b) #remainder
print(a // b) #quotient
print(a ** b) #power a^b

#relational/comparison operators
# ==,!=,>,<,>=,<=
#{output always false/true}

a = 20
b = 70
print(a == b) #equal
print(a != b) #not equal
print(a > b) #greater than
print(a < b) #less than
print(a >= b) #greater than or equal to
print(a <= b) #less than or equal to


#assignment operators
# =,+=,-=,*=,/=,%=,//=,**=

num = 10
#both are same
num = num + 10 #10+10 => 20
num += 10 
print("num :", num)
num -= 2
print("num :", num)
num *= 5
print("num :", num)
num /= 2
print("num :", num)
num %= 5
print("num :", num)
num //= 5
print("num :", num)
num **= 5
print("num :", num)

#logical operators
#and,or,not

#and
val1 = True
val2 = False
print("AND operator :", val1 and val2)

#or
val1 = True
val2 = False
print("OR operator :", val1 or val2)

#not
val1 = True
val2 = False
print("NOT operator :", not val1)
print("NOT operator :", not val2)