a=300
if a==300:
    print("yes its is greater")
else:
    print("no its not equal")
# --------------------------*******************--------------------
a=300
if a==3003:
    print("yes its is greater")
else:
    print("no its not equal")
# --------------------------*******************--------------------
a=300
b=400
if a>b:
    print("a is greater than b")
    print("your calculation is correct")
else:
    print("Wrong calculations")
# here "if" is a keyword, "a>b" is a expression which reads by interpretor if its true interpretor executes if  its
# not true it do not execute. Entering after placing colon leads to block of "if" statement.
# --------------------------*******************--------------------
#                        How facebook login system works
# how if-else statement works?
# when we run code which include if-else statement when interpretor comes to if-else statement it checks the condition
# which we give to if-statement if its true it direct execute if's block and if its not true it direct executes
# else's block just after checking the if's condition
username="Bilal Haneef"
password="MBHQ"
if username=="Bilal Haneef" and password=="MBHQ":
    print("Welcome " + username)
else: 
    print("Please check your username and password")
# --------------------**********************------------------
#                          Nested if
# Nested if is defined as "if inside if".
# nested if work by checking if conditions line by line in the code below interpretor reads line 41 and after reading
# line 41 it executes the first if block which is true after which it checking every if block and executes it which
#  is quite time taken.Therefore "elif" comes into play.
a=5
if a==5:
    print("Yes!")
    if a==4: 
        print("no 1")
    if a==7:
        print("no 2")
    if a==6:
        print("no 3")
else:
    print("Wrong Prediction")
#  --------------------------*********************--------------------------
# in the lines below what we do is just use elif instead of if because we can save time of interperator by this 
# if the condition of line 55 is true then interpretor direct executes if's block and it dont need to read next 
# elif statements. Precisely, "if condition of first if is not true then if will go for the next one".
a=5
if a==5:
    print("Yes! its true")
elif a==3: 
    print("no 1")
elif a==4:
    print("no 2")
elif a==6:
    print("no 3")
else:
    print("Wrong Prediction")