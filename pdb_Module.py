import pdb

# what is debugging? 
# Debugging is the process of finding and resolving defects or problems within a computer program that prevent
# correct operation of computer software or a system

# why debugging?
# 1) our program is not running and causing unexpected errors.
# 2) our program is running but not working the same way we want.

# steps for debugging
# 1) set_trace (pdb module's function)
# 2) execute code line by line

# in this code below i have made mistake which im gonna find usnig pdb module. This is very small coe what if we have
# hundereds and thousands lines of code so pdb module will help on that situation
pdb.set_trace() # this will stop my execution after every reading every single line
# in this case it will first read line no 20 and stop and if i want to check on which line it is present i'll type 
# "l" which will tell my line no and to move it on next line i'll type "n" which will debug next line and stop
# so  in this way it will let me know which line is causing error and we can fix the error easily
name = input("Enter your name :")  
age = input("Enter your age :")  
print(f"hello {name} your age is {age}")
age2 = int(age) + 5
print(f"{name} you will be {age2} in next five years")

# l = line no
# n = next line
# c = continue (run our program wiht out stopping on every line) 
# q = quit

# we can write set_trace on the above line we think can cause error