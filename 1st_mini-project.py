# GUESS THE NUMBER
'''
import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or Quit(Q) :")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number is too small. Take a bigger guess..")
    else:
        print("Your number is too big. Take a smaller guess..")

print("----- GAME  OVER -----")
'''

# RANDOM PASSWORD GENERATOR
'''
import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("Your random password is :", password)
'''

#OR

import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function for i in range(n)]
password = "".join([random.choice(charValues)for i in range(pass_len)])

print("Your random password is :", password)