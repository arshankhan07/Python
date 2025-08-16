#when a string is created, it is stored in the memory as a sequence of characters.
#each character is assigned a unique index number(position).
#the index number is used to access the character at a specific position in the string.
#the index number starts from 0 and goes to n-1 where n is the length of the string.
#it starts from left to right and always starts from 0 not 1.
#it counts the spaces and special characters also.
#it is used to direct access the character at a specific position in the string.

str = "Hello World"
ch = str[0]
print(ch)


#SLICING

#slicing is used to get a part of the string.
#it is used to get a substring from the string.
#it is used to get a part of the string from a specific position to another position.
#it provides the value of the string in a range of index numbers.
#starting_ind : to  ending_ind : . i.e. starting_ind to ending_ind-1.

str = "Hello World"
print(str[1:4]) #or we can write, print(str[1:len(str)]) to go to the last index.
# or we can write, print(str[1:]) to go to the last index.
# or we can write, print(str[:4]) to go to the first index.
# or we can write, print(str[:]) to go to the last index.
# or we can write, print(str[::2]) to skip the characters.
# or we can write, print(str[::-1]) to reverse the string.

#NEGATIVE INDEXING

#negative indexing is used to access the string from the end. i.e from right to left.
#it starts from -1 and goes to -n where n is the length of the string.

str = "Hello World"
print(str[-3:-1]) #or we can write, print(str[len(str)-1]) to go to the last index.

#we can also use negative indexing to skip the characters.
print(str[-3:-1:2]) #or we can write, print(str[len(str)-1:-1:2]) to go to the last index.

#we can also use negative indexing to reverse the string.
print(str[-1::-1]) #or we can write, print(str[len(str)-1::-1]) to go to the last index.

#str.endswith() -> checks if the string ends with the specified character.

str = "Hello World"
print(str.endswith("d"))
"""print(str.startswith("H"))
print(str.isalpha())
print(str.isdigit())
print(str.isalnum())
print(str.isspace())
print(str.islower())
print(str.isupper())"""

#str.capitalized() -> converts the first character to uppercase and rest to lowercase.
#str.replace("old","new") -> replaces the old character with the new character.
#str.count("char") -> counts the number of times the character appears in the string.
#str.find("char") -> finds the index of the character in the string.
#str.index("char") -> finds the index of the character in the string.
#str.isalnum() -> checks if the string is alphanumeric.
#str.isalpha() -> checks if the string is alphabetic.
#str.isdigit() -> checks if the string is numeric.
#str.isspace() -> checks if the string is space.
#str.islower() -> checks if the string is lowercase.
#str.isupper() -> checks if the string is uppercase.