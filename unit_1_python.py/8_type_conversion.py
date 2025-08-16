#converting one variable to another type.
# like converting int to float, float to int, int to string, string to int, etc.

# two types of conversion : 
# 1. type conversion -> automatic conversion
# 2. type casting -> manual conversion

# 1. implicit type conversion
# 2. explicit type conversion

# implicit type conversion
# python automatically converts one data type to another data type.
# explicit type conversion
# we can convert one data type to another data type using type casting.

# type conversion (implicit conversion)
a = 2 
b = 3.5
sum = a + b
print("sum :", sum)

# type casting (explicit conversion)
a = int("2") 
b = float("3.5")
sum = a + b
print("sum :", sum)