# input function always takes data from user in form of string
# name = input("Whats your name?")
# print( "Your name is " + name )
# age = input("Whats your age?")
# print("Your age is " + age)
# Now we use input function in one line
name, age = input("Enter your name and age ").split(".") # whatever we use in parenthesis of split function it works as splitter
# here we use space b/w split function
print(name)
print(age)