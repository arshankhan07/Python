# FILE I/O IN PYTHON. 
# python can be used to perfom operation on a file. (read and write data)

""" TYPES OF ALL FILES
1. Text Files : .txt, .docx, .log etc.
2. Binary Files : .mp4, .mov, .png, .jpeg etc."""

# OPEN, READ & CLOSE FILE
#we have to open a file before reading or writing.

#f = open("file_name", "mode")

""" here file name can be (sample.txt, demo.docx)
and mode can be r: read mode, w: write mode
and in python, bydefault mode is read mode"""

f = open("my.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

"""
characters: meanings
r : opens for readding (default)
t : text mode (default)
w : opens for writing, truncate the file first (delete the text and write new text)
x : create a new file and pens it for wrriting
a : open for writing, appending to the end of the filee if it ecists
b : binary mode
+ : open a disk file for updating (reading and writing)
r+ : read + over write(pointer at start) -> no truncate
w+ : read + over write(pointer at start) -> truncate
a+ : read + append (pointer at end) -> no truncate
"""