# module - python file contain usefull classes and functions wrote by developers
# A file containing Python code, for example: example.py, is called a module, and its module name would be example.
# We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.
# We can define our most used functions in a module and import it, instead of copying their definitions into different programs.
# so i have already created a file named calculation.py which we can say a module 
# We use the import keyword to do this. To import our previously defined module calculations, we type the following in the Python prompt.
import calculations 
# Using the module name we can access the function using the dot . operator. For example:
# print(help(calculations))
print(calculations.add(2,8))
print(calculations.floor_div(9, 0))
print(calculations.floor_div(9, 9))
#  thats how i can create and use my modules 
# ____________________________________________________________________________________________________________________________________________
# Python has tons of standard modules. You can check out the full list of Python standard modules and their use cases. These files are in the 
# Lib directory inside the location where you installed Python.
# Standard modules can be imported the same way as we import our user-defined modules.
# ____________________________________________________________________________________________________________________________________________

import math
print("The value of pi is", math.pi)
print(math.cos(0))
# ____________________________________________________________________________________________________________________________________________

# Import with renaming
# We can import a module by renaming it as follows:
# ____________________________________________________________________________________________________________________________________________

import math as m
print("The value of pi is", m.pi)

# We have renamed the math module as m. This can save us typing time in some cases.
# Note that the name math is not recognized in our scope. Hence, math.pi is invalid, and m.pi is the correct implementation.
# ____________________________________________________________________________________________________________________________________________

# Python from...import statement
# We can import specific names from a module without importing the module as a whole. Here is an example.
# for e.g. import only pi from math module
from math import pi
print("The value of pi is", pi)

from math import pi,e
print(f"value of pi is {pi} and value of exponential is {e}")
# ____________________________________________________________________________________________________________________________________________

# Import all names
# We can import all names(definitions) from a module using the following construct:
# import all names from the standard module math

from math import *
print("The value of pi is", pi)
print("The value of e is", e)
print(factorial(3))
print(cos(0))
print(sin(0))
print(tan(0))
# Here, we have imported all the definitions from the math module. This includes all names visible in our scope except those beginning with 
# an underscore(private definitions).
# Importing everything with the asterisk (*) symbol is not a good programming practice. This can lead to duplicate definitions for an identifier.
# It also hampers the readability of our code.
# ____________________________________________________________________________________________________________________________________________

# now if we want to know all the function in modules then we use dir() function. This show all function and its variables
import module1 
x = dir(module1)
print(x)