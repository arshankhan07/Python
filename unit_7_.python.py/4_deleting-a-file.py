# DELETING A FILE
# usin the os module
# module (like a code liberary) is a file written by another programmer that generally has a function wee can use.

# import os
# os.remove(file-name)

"""import os 
os.remove("sample.txt")"""

# Q: Create a new file "practice.txt" using python. Add the following data in it:
"""Hi everyone
we are learning file I/O
using Java.
I like programing Java"""

'''with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programing Java")'''

# Q: WAF that replaces all occurrences of Java with python in above file

'''with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)'''

# Q: Search if the word "learning" exist in the file or not.

'''word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")'''

# Q: WAF to find in which line of the file does the word "learning" occur first.
# print -1 if word not found.

'''def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("found")
        else:
            print("not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.read()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())'''

# Q: From a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("numbers.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)