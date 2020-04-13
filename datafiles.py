# we can read,write and append file in python 
###################### for reading #########################
# what if we want to read the existing file, we use read mode for this
# open function returns a handler which has no name and we need to suggest the name of the handler
# we can change name of handler as our wish as we change here as work its up to us
with open("Test.txt","r") as work:
    a = work.read()
# whenever we came out of the indentation interpretor termed it as work done and closes the file
    print(a)
# what if we want to write something in our file for this we use write mode
###################### for writing #########################
with open("Test.txt","w") as work:
    work.write("This is not a test file")
############################################################
# now our file has been overwritten with what we had passed in write braces
with open("Test.txt","r") as work:
    a = work.read()
    print(a)
# write mode will overwrite on what written in file prior
# if we want to read a non-existing file interpretor will give an error "No such file is found" 
# with open("Testing.txt","r") as file:
#     b =  file.read()
#     print(b)
# if we want to write a non-existing file interpretor will create a file and overwrite in it
with open("Testings.txt","w") as New:
    New.write("Testing this a non-existing file")
with open("Testings.txt","r") as New:
    c = New.read()
    print(c)
# what if we want to write in file without overwriting the previous data
# we use append mode for this task
with open("Testings.txt","a") as New:
    New.write(" Appeding some text to look how this works")
with open("Testings.txt","a") as New:
    New.write(" It works as expected")
with open("Testings.txt","r") as New:
    o = New.read()
    print(o)
# what if we want to read and write the file at the same time we use w+ mode for this purpose
with open("newText.txt","w+") as first:
    first.write("This a another text file")
# when we use read mode here(right after write mode) w+ mode will now show our file data interpretor reads write lines
# before read mode
    first.seek(0) # now interpretor starts reading our file from 0 index
    print(first.read())
# another mode(r+) we have provide facility of reading and writing
# if file isn't exist in system r+ mode will give an error
# this will overwrite the previous text
with open("newText.txt","r+") as first:
    first.write("This is another fileeeee 1")
    first.write("This is another fileeeee 2\n")
    first.write("This is another fileeeee 3\n")
    first.seek(0)
    print(first.read())
