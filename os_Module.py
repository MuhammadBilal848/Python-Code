import os
# Python - OS Module
# It is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating and removing 
# a directory (folder), fetching its contents, changing and identifying the current directory, etc.

# __________________________________________________________________________________________________________________________________________

# Creating Directory
# We can create a new directory using the mkdir() function from the OS module.
# os.mkdir("os_check") # this will create folder named "os_check" in my current directory (python-git)
# os.mkdir("C:\\os_check") # this will create folder named "os_check" in my C drive

# # __________________________________________________________________________________________________________________________________________

# # Changing the Current Working Directory
# # We must first change the current working directory to a newly created one before doing any operations in it. This is done using the
# # chdir() function.
os.chdir("C:\\")

# There is a getcwd() function in the OS module using which we can confirm if the current working directory has been changed or not
# cwd = current working directory
print(os.getcwd())

# __________________________________________________________________________________________________________________________________________

# if we want to check whether a file is present in a directroy or not , we can use os.path.exit('file-path') method which return boolean
# values
print(os.path.exists('os_check')) 

# __________________________________________________________________________________________________________________________________________
                                                            # Extra Commands

os.chdir("C:\\os_check")
print(os.getcwd())

# __________________________________________________________________________________________________________________________________________

# how to create files in os module
open("file.txt","a").close()

# __________________________________________________________________________________________________________________________________________

# how to check how many files are there in a directory , for this we can use listdir()  which create list of all the files present in drty
print(os.listdir("C:\\os_check"))

# __________________________________________________________________________________________________________________________________________

# the above method listdir will print all the files present in a directory but not the path of files, so to create path of files 
for a in os.listdir("C:\\os_check"):
    path = os.path.join(os.getcwd(),a)
    print(path)

# __________________________________________________________________________________________________________________________________________

# how to check how many files and folders are thre in my directory also want to check the folder inside folder and files inside that folder
# for this we use walk method that is an iterator object and if i looped over this it will return current_path,folder_names,file_names

itera = os.walk("C:\\os_check")
print(itera)
for current_path,folder_names,file_names in itera:
    print(f"current path : {current_path}")
    print(f"folder name : {folder_names}")
    print(f"file names : {file_names}")

# __________________________________________________________________________________________________________________________________________

# if we want to make folder inside folder we use makedirs() method
# os.makedirs("hello1/hello2")

# __________________________________________________________________________________________________________________________________________

# if we want to remove directory , we can use rmdir() method that removes only those directories that are empty , if directiry is not empty 
# it will causse error
# os.rmdir("document")
# os.rmdir("poool") # folder has been deleted thats why we comment this line so that it cant cause error
 
# to delete directory that is not empty we need to import 'shutil' module that has rmtree() method which help deleting this file
import shutil
# shutil.rmtree("hello1") # this will remove the directory completely from the machine and will not show in recylebin

# if we want to copy a folder that and want to paste that folder in another directry we use copytree() method
# suntax - shutil.copytree("copied-file-path","where-to-copy-path/copied-file-name(we can also rename filehere")
# shutil.copytree("hello1","document/hello1") # so here im making a copy of hello1 directory in document directory

# if we want to copy a file we use copy method
# shutil.copy("file.txt","document/file.txt")

# if we want to move the file/folder to another folder/file  we use move() method
# suntax - shutil.copytree("moved-file-path","where-to-copy-path/moved-file-name(we can also rename filehere")
shutil.move("file2.txt","songs\\")