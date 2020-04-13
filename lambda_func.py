# lambda expression/function is also known as anonnymous function
# lambda function is a function which we define in one line and has no name
def add(a,b):
    return a+b
# print(add(2,3))
# in the above code we made a simple function 
# now we made this function using lambda function
# syntax of lambda function, lambda variable(comma separated) : return-value
sum_1 =lambda a,b : a+b # assigning lammbda function to any variable dont
# print(sum_1(2,6))
#########################################################################
def even(a):
    return a%2==0
# print(even(5))
# now we made the above function using lambda 
even1 = lambda a : a%2 == 0 
# print(even1(3))
##########################################################################
def str_char(s):
    return s[-1]
# print(str_char("Hello"))
# now we made the above function using lambda 
char = lambda a : a[-1]
# print(char("World"))
################################# Using if-else in lambda function ###########################
def func_1(a):
    return len(a) > 5
print(func_1("Hello"))
func = lambda s : True if len(s) > 5 else False
# print(func("Higher"))
################################ Enumerate function ####################################
enumera
list = ["bilal","hamza","zeehan","wassay","rayan"]
for ind,val in enumerate(list):
    print(f"{ind} has this value {val}")