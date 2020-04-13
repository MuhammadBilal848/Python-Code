# Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module
#  can also include runnable code
# -------------OR-----------------
# a module is a file containing python definitions and statement
# all the files in module have .py extension
# now creating a module 
# i have made separate python program named "module1" which contain function which performs addition
# now we use this module using import statment
import module1
module1.add(5,5)
# now naming of module
# we can change module name as our requirement using "as" keyword
import module1 as math 
math.add(3,7)
math.sub(5,5)
math.mult(5,5)
math.div(81,9)
# lets take a example of python buit-in-module which is platform
# python buit-in-module which is platform let us know which OS we are using
# import platform
# a = platform.system()
# print(a)
# now if we want to know all the function in modules then we use dir() function. This show all function and its variables
import module1 
x = dir(module1)
print(x)