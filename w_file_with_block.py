# with is block is an other method to read / write files

print("                                         reading a file")
with open("Test.txt","r") as a:  # is we dont pass second argument it reads the file by default , here "a" is called "alias" which acts as var
# name and use to read/ write files 
# there is no need to close file in "with block" , it close the file it self.
    data = a.read()
    print(data)
print(a.closed) # this data discriptor will return True because file has been closed

print("                                         writing a file")
# to write file we can use "w","a","r+"
# what "w" do is it will help me write into my file by over-writing(previous data got erased)
# with open("Testings.txt","w") as a1:
#     a1.write("Hello")
# we have to use "w" mode when our file is empty
# if a file doestnt exit , "w" mode will create the file it self and write in it    

# _____________________________________________________________________________________________________________________
# if we dont want to over-write our file but we want to continue writing after the data that present in our file , we use "a" mode which is 
# append mode
with open("Testings.txt","a") as a3:
    a3.write("\n Hello............................")
# if a file doestnt exit , "a" mode will create the file it self and write in it    
# _____________________________________________________________________________________________________________________
# "r+" mode will never create a file if it not exist , instead it will generate error 
with open("Testings.txt","r+") as b:
    b.write("Hello Bilal")
# "r+" mode Opens a file for reading and writing, placing the pointer at the beginning of the file. and start over-writing character by 
# character(means all the characters that present in write parenthesis will substitute the same number of character present in file)
# _____________________________________________________________________________________________________________________
# what if we want to read and write at the same time , for this we can do this
with open("file1.txt","r") as f1:
    with open("file2.txt","w") as f2:
        f2.write(f1.read())
a = open("file2.txt","r")
print(a.read())