# Decorators - enhance the functionality of other functions

# on line 11 we have simple function that prints a single line and we want this function to print another line but not by changing this function,
# by decorator function
def decorator_function(any_func): # this dec_function takes any function as parameter(which functionality needs to be enhance)
    def wrapper():
        print("This is decorator function's line")
        any_func()
    return wrapper
# in the above code i defined my decorator function that takes any function(which functionality needs to be enhance) as argument and return
# wrapper which itself a function that prints a line after which user's given parametric function get called and performs its work
# function "wrapper" that prints a line and 

def sim_func():
    print("This is simple function")

var = decorator_function(sim_func) 
# here i called dec_func and passed my sim_func as parameter so now what interpretor do is it will return wrapper func which get stored in var 
# but to access it i need to put braces()
var() # when i put braces in var it will become wrapper function and here by putting braces im calling it and that prints a single line after
# which my sim_func get called and do its work.
 
# now decorators have another thing called "syntactic sugar"
# @ use for decorators
# and thats an easy way to apply decorator
@decorator_function #  after this i defined my function(which functionality needs to be enhance) in the next line
def sim_funct():
    print("This is simple function")
sim_funct()
# ________________________________________________________________________________________________________________________________________
# what if i define a function that takes argument and i want to apply decorator in it
# @decorator_function # here i applied my decorator on square function
def square(n):
    return n**2 
square(5) 
# so this will generate error 
# the reason behind generating error is ,
# here if i apply decorator(by commenting syntactic sugar) by other method
# varo = decorator_function(square) # here i called dec_func and passed my square_func as parameter now interpretor will store my wrapper function 
# in varo and to access it i need to put braces()
# varo() # here by putting braces im calling wrapper func that print its line after which my square function get called but square needs one
# argument and arguments has not given so thats the reason why its giving error
# ________________ Changing my decorator function ______________________
def decorator_function1(any_func): 
    def wrapper(*args,**kwargs): # so here i give wrapper function args and kwargs which will prevent error 
        """ This wrapper function doc string """
        print("This is decorator function's line 1")
        return any_func(*args, **kwargs)  # and here when wrapper get called it will call my given parametric func which will return square but we need
# that number so we again return that number so that we can use it and display as ouput
    return wrapper

@decorator_function1
def square1(g):
    """ This is square function doc string """
    return g**2

print(square1(5))

print(square1.__doc__) # this will show wrapper func docstr instead of square1 func
print(square1.__name__) # this will show wrapper func name instead of square1 func
# to prevent this happening i need to import wraps from functools
# from functools import wraps

# print(square1.__doc__) 
# print(square1.__name__)

from functools import wraps
def deco_func(any_func):
    @wraps(any_func) # if we want to access our function name we have to use this built in decorator wraps that allow us to access our func name
    def wrapper(*args,**kwargs):
        print(f"You are calling {any_func.__name__} function")
        print(any_func.__doc__)
        return any_func(*args,**kwargs)
    return wrapper
        
@deco_func
def add(a,b):
    """This function takes two numbers as parameter and return their sum """
    return a+b

# e = deco_func
print(add(3,3))
