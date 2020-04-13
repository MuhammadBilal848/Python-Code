name=input("Type your name ")
print("Hello! " + name)
# important thing about input func. is that it always takes input in form of string.
age=input("Type your age ")
print(name + " your age is " + age)
# what if we want to get two or more input by just writing a single line of code.
name,age=input("Type your name and age comma separated: ").split(",")
# in the above line on code(7) any thing which we will write in double quotes will be used as separator.
print("Your name is " + name+ "\n" +"your age is " + age)
# -------------------***************************----------------
# write program which takes input of your age and if you are under 18 it prints you are under age.
age=int(input("Whats your age? "))
print(age)
if age>=18:
    print("You are in.")
else:
    print("You are under age")



