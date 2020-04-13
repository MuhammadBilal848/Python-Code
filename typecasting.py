# # the changing of str to int, int to str, int to float is called "Type Casting"
# a = input("Enter your name: ")
# print(type(a))
# # -----------***********------------
# a = int(input("Enter any number: ")) # we type cast str to int
# print(type(a))
# # -----------***********------------
# a = float(input("Enter any number: "))
# print(type(a))
# # -----------***********------------
# a = input("Enter your name: ")
# print(a.lower())
# # -----------***********------------
# a = input("Enter your name: ")
# print(a.upper())
# # -----------***********------------
# a = input("Enter your name: ")
# print(a.title())
# # -----------***********------------
a = input("Enter your username: ")
b = a.title()
if b=="Muhammad Bilal Haneef Qureshi":
    print(f"Welcome {b}")
else:
    print("Check your username")