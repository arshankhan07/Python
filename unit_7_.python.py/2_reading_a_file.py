"""data = f.read() #reads entire file
   data = f.readline() # reads one line at a time
"""
f = open("my.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

# READING A FILE

f = open("my.txt", "w")
f.write("i want to learn py")
f.close()