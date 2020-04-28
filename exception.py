# ___________________________________________________________ Built-in Errors ______________________________________________________________
# EOF-Error	Raised when the input() function hits the end-of-file condition.
#       print("h"
# NameError	Raised when a variable is not found in the local or global scope.
#      print(1+"g")
# IndexError	Raised when the index of a sequence is out of range.
#       l = [1,2,3]
#       print(l[4])
# ValueError	Raised when a function gets an argument of correct type but improper value.
#         a = "abc"
#         print(int(a))
# AttributeError	Raised on the attribute assignment or reference fails.
#         l = [1,2,3]
#         l.push(2)
# KeyError	Raised when a key is not found in a dictionary.
#         d = {"name":"Bilal"}
#         print(d["Age"])
# StopIteration	Raised by the next() function to indicate that there is no further item to be returned by the iterator.
#         a = map(lambda a : a*2,[1,2])
#         print(next(a))
#         print(next(a))
#         print(next(a))
# SyntaxError 	Raised by the parser when a syntax error is encountered.
#         print(
# IndentationError	Raised when there is an incorrect indentation.
#         def s():
#         print("Hi!")
#         s()
# TabError	Raised when the indentation consists of inconsistent tabs and spaces.
# TypeError	Raised when a function or operation is applied to an object of an incorrect type.
#         def l_sum(l):
#             b = 0
#             for a in l:
#                 b += a
#             return b
#         l_sum(3)
# ImportError 	Raised when the imported module is not found.
# ZeroDivisionError	Raised when the second operand of a division or module operation is zero
# RuntimeError	Raised when an error does not fall under any other category.

# ______________________________________________________________ Raising Errors _______________________________________________________________
# e.e we have a function that adds two number and return their sum , what if user pass numbers in form of string , fucntion will concatenate 
# input instead of addition , so i can raise erro for this
# first we solve this prolem using if else
 
def add(a,b):
    if ((type(a)) is int) and (type(b) is int):
        return a+b
    # return "Oops you are passing wrong data type to the function"
    raise TypeError("Oops you are passing wrong data type to the function")
# in real world programmming we dont return errors like the way we did above(line # 49), for this we use raise keyword and identify that error
# and write our desired string in that error's braces, so in the above case its typeerror thatswhy we have written TypeError
print(add(1,1))
print(add(1,"2"))     

class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
#         return "This is animal sound"
        raise NotImplementedError("You have to create sound function first in your child class")
class Dog(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color
class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color
cat1 = Cat("Billi","White")
print(cat1.sound())
# now i want to raise error if any of my child class doesnt have sound function , So what i do is i will raise notimplemented
# error in my sound function of parent class
# this type of methods in which we raise notimplementederror is called abstract method( line # 59)


# ___________________________________________________ Exception Handling ________________________________________________________________
# we use exception handling in python when we expect some sort of unexpected output
# age = int(input("Enter your age here: "))
# if age>=18:
#     print("Yes you can play")
# else:
#     print("You can't play")
# in the above code user input a number(integer) to know whether he is underage or not 
# what if user give input in string format(seven,eight,.........)
# interpretor will give error so here we use exception handling to overcome this problem
# first we have to decide which line can cause error
# and the line which cause error we write that line in try's block
while True:
    try:
        age = int(input("Enter your age here: "))
        break # when ever user input right value(int), break will be executed
# we can write multiple lines of code in try's block as per requirement 
# if any anyline of code generate error in this block interpretor will not execute those lines it just works as "if"
    except ValueError: # here we can also use valueError because we are supposing that here must be a value error
# in python as any other languages we should only handle those exceptions which we think can generate a error
# this will save time of interpretor not to search in libraries or classes to find which error is that
        print("Invalid Input...................")
# if the expected error isn't a ValueError we will write another exception 
    except:
        print("Unexpected Error") # all those exce. which are not valueerror, handeled by this exception
# we can write multiple lines of code in try's block as per requirement 
# when the code present in try's block generate error except block will execute it just works as "else"
# python uses another keyword in exception handling "Else", if try block successfully executed interpretor directly
# execute else block in other words if try block wont have any exception else block will execute  
    else:
        if age>=18: # here indentation is not important because "age" variable will form already from try's block
            print("Yes you can play")
        else:
            print("You can't play")
# now we have another keyword "Finally", finally's block will always execute whether the code in try's block has exception or not
    finally:
        print("Finally is executed")