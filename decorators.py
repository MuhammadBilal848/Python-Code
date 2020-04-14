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
# but to access it i want to put braces()
var() # when i put braces in var it will become wrapper function and here by putting braces im calling it and that prints a single line after
# which my sim_func get called and do its work.
 
# now decorators have another thing called "syntactic sugar"
# @ use for decorators
# and thats an easy way to apply decorator
@decorator_function #  after this i defined my function(which functionality needs to be enhance) in the next line
def sim_funct():
    print("This is simple function")
sim_funct()


