# # input function always takes data from user in form of string
# name = input("Whats your name?")
# print( "Your name is " + name )
# age = input("Whats your age?")
# print("Your age is " + age)

a,b = input("Enter your name and age ").split(",")
print(a,b)