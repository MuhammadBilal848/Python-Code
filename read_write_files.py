# read file
# open function 
# read method
# seek method
# tell method
# readline method
# readlines method
# close method


# to read file use open function which takes two arguments
# syntax - open(file, mode)
# file	The path and name of the file
# mode	A string, define which mode you want to open the file
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist
# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
#  _________________________ OR ____________________________________
# r
# Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

# rb
# Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.

# r+
# Opens a file for both reading and writing. The file pointer will be at the beginning of the file.

# rb+
# Opens a file for both reading and writing in binary format. The file pointer will be at the beginning of the file.

# w
# Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

# wb
# Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

# w+
# Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

# wb+
# Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

# a
# Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

# ab
# Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

# a+
# Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

# ab+
# Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.


print("                                         reading a file")
print("                                         a")
a = open("Test.txt","r")
# so if we want to read the file we use "r" mode which is read mode and if i dont mention any mode , read mode is already set to default
# now this is my file object stored in var a in line no 23 which can be looped over, to read this file stored in a we use "read method"
print(a.read()) # read method will return my text file data
# now we have to close our file , but if we dont close our file it will cause problem so thats a good practice to always close file 
a.close()

# ________________________________________________________________________________________________________________________________________

print("                                         a1")
a1 = open("Test.txt","r")
# what if i apply read method multiple times on var a1 it will print my text file only once
print(a1.read())
print(a1.read())
a1.close()

# so why is it hapenning that our data gets print only once, read mode will always read our file with our cursor movement which is left to 
# right or from first word to the last word, so when my read mode(on line # 32) reads the last word of the text file while reading the file
# it has nothing left to read thats why next read method (in line # 33) is not working 

# ________________________________________________________________________________________________________________________________________

print("                                         a2")
# if we want to check our cursor position we use tell method
a2 = open("Test.txt","r")
print(a2.tell(),"cursor starting position")
print(a2.read())
print(a2.tell(),"cursor ending position")
a2.close()

# ________________________________________________________________________________________________________________________________________

print("                                         a3")
# now if we want to change the cursor's position , for this we use seek method
# so we want to read our file two time in this code so we can chenage the cursor postition to 0 by which interpretor will again start reading 
# the file again
a3 = open("Test.txt","r")
print(a3.tell(),"cursor starting position")
print(a3.read())
print(a3.tell(),"cursor ending position")
a3.seek(0)
print(a3.tell(),"cursor starting position")
print(a3.read())
print(a3.tell(),"cursor ending position")
a3.close()

# ________________________________________________________________________________________________________________________________________

print("                                         a4")
# what if we want to read only single line of our text file, for this we juse  readline method
a4 = open("Test.txt","r")
print(a4.readline())
print(a4.readline())
print(a4.readline())
a4.close()

# ________________________________________________________________________________________________________________________________________

print("                                         a5")
# what if we want to add all the lines of our text file in list we use readlines method
a5 = open("Test.txt","r")
lines = a5.readlines() # this has converted my file into list
print(lines)
print(len(lines))

# ________________________________________________________________________________________________________________________________________

print("                                         a6")
# now what if we want to check our file name for this we can use data discriptor "name"  means we need to punt parenthesis after them
# another data discriptor we use is "closed" to check our get closed or not it will return boolean values
a6 = open("Test.txt","r")
print(a6.name)
print(a6.closed) # now this will return False b/c file is open
a6.close()
print(a6.closed) # now this will return True b/c file is clase

# ________________________________________________________________________________________________________________________________________

print("                                         f")
# what if our file in not in the same directory but in different directory we need to write that path of that file 
f = open(r"E:\new_file.txt") # so this line will cause error because single back slash(\) in python treated as escape sequence so to tackel this
# we can use make the string a raw string by putting "r" before the string

print("                                         writing a file")
a = open("filo.txt","a") # append "a" mode will create file if if does not exists
a.write("Hello this file is made by using append mode")

# we can also append a new text to the already existing file or the new file. using "a+" mode
b = open("filo.txt","a+") 
b.write("\n trying a+ mode")