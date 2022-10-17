# Open file in read/text mode (default mode)
fileobj = open("E:/Python/test.txt")
# Open file in read mode
fileobj = open("E:/Python/test.txt", 'r')
# Open file in write mode
fileobj = open("E:/Python/test.txt", 'w')
# Open file in append mode
fileobj = open("E:/Python/test.txt", 'a')

# Close the file
fileobj.close()

# Read File
fileobj = open('E:/Python/test1.txt')
# Read whole file
print(fileobj.read())
# File cursor is already at the end of the file so it wont able to read.
#print(fileobj.read())

# Bring the file to intial position
fileobj.seek(0)
# print(fileobj.read())

# Place file cursor at position 7
fileobj.seek(7)
# print(fileobj.read())

fileobj.seek(0)
# Read first 22 characters of the file.
print(fileobj.read(22))

# Get the file cursor position
print(fileobj.tell())

# readline() - Reads the line of a file
fileobj.seek(0)

print(fileobj.readline())  # Read first line of a file

print(fileobj.readline())  # Read sencond line of a file

# readlines() - Read all lines of a file
fileobj.seek(0)
print(fileobj.readlines())

# Read first 5 lines of a file using readlines()
fileobj.seek(0)

count = 0
for i in fileobj.readlines():
    if (count < 5):
        print(i)
    else:
        break
    count += 1

# Write File
fileobj1 = open('E:/Python/test2.txt', 'w')
# Add content to existing file
fileobj1.write('This is the new content appended in the existing file.')
fileobj1.close()

fileobj1 = open('E:/Python/test2.txt', 'r')
print(fileobj1.read())

fileobj1.close()

# Open the file in append mode to add new data 
fileobj2 = open('E:/Python/test2.txt', 'a')
fileobj2.write('Open the file in append mode. Add new content to existing file.')
fileobj2.close()

fileobj2 = open('E:/Python/test2.txt', 'r')
print(fileobj2.read())
fileobj2.close()

# Delete File
import os
os.remove("E:/Python/test2.txt")

# This is python code to take analogy of with()
with open('E:/Python/test.txt') as file:
    data = file.read()

with open('E:/Python/test.txt', "w") as file:
    file.write("Hello World")

# Analogy for using split() function
with open("E:/Python/test1.txt", "r") as file:
    data = file.readlines()
    for line in data:
        # splits each line sentence into words
        word = line.split()
        print(word)





