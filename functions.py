# in python we define functions so that we dont need the write the code multiple times for the same task
# A function is a block of code which only runs when it is called.
# function can neither operated itself we have to call it when we want to use it
# interpretor never enter in functions body untill we call it
def add(): # this type of function is called parameter less function
    num_1 = int(input("Enter your first number: "))
    num_2 = int(input("Enter your second number: "))
    print( num_1 + num_2 )
# now we are calling function  
add()
# ------------------*****************--------------------
# Function: passing information positional arguments
# here num1 and num2 are parameters
# when we call this function we have to provide arguments to this function 
# "Argument is any value which passes to a parameter"
# when we call this function num1 and num2 assingn to their respective parameters and this assignment is positional 
# thats why its called passing information positional arguments
# # this type of function is called parameterized function
def add_1(num1,num2): # here num1 and num2 are called "parameters" 
    print( num1 + num2 )
add_1(2,8) # here 2 and 8 are called "Aruguments"
# ------------------*****************--------------------
# Function: passing information keyword arguments
# in this type of function sequence does'nt matter we just have to assign the number or word as argument
def full_name(first,middle,last):
    print( first + middle + last )
full_name("Muhammad ","Bilal ","Haneef")
# we can direct call function and give function its arguments but what if we want to pass arguments in different order
# such as (last,middle,first)
full_name( last="Haneef" , first="Muhammad " , middle="Bilal " )
# here's a thing to remember we have to pass argument in sequnce
# full_name("Muhammad","Bilal",first="Haneef") # it gives an error because we already pass value to first argument
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before 
# the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def FName(**name):
    print(name["fname"])
FName(fname="Bilal",mname="Haneef",lname="Qureshi")
# ------------------*****************--------------------
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:    
# kwargs -------------------> arbitrary keyword argument
def name(**kwargs):
    print(kwargs)
    print(type(kwargs))
name(f_name="Muhammad",s_name="Bilal",l_name="Haneef",age=20) # i can give as many agument as i want.
# kwargs with other parameters
def namel(name,**kwargs):
    print(name, kwargs)
# namel(f_name="Muhammad",s_name="Bilal",l_name="Haneef",age=20) in this line we havenot given name first positinal argument due to which it gives error
namel("Hello",f_name="Muhammad",s_name="Bilal",l_name="Haneef",age=20)
# dictionary unpacking
def man(**kwargs):
    for a in kwargs.items():
        print(a)
# man(f_name="Muhammad",s_name="Bilal",l_name="Haneef",age=20)
d = {'f_name': 'Muhammad', 's_name': 'Bilal', 'l_name': 'Haneef', 'age': 20} 
man(**d)  # here ** use for dictionary unpacking
# **d = { f_name = 'Muhammad', s_name = 'Bilal', l_name = 'Haneef', age = 20 } thats how unpacked dictionary looks like(we cant print this its 
# just an explaination)
# ------------------*****************--------------------
# Function: default value parameter(default parameters should be at last of all parameters)
# what if we define function and user calls it but not provide arguments to function
# here's default value parameter comes into play what we do is we already provide function default parameters such that
# when user do not pass arguments so those bu default values will print
def fulln( first=" " , middle=" " , last=" " ):
        print( first + middle + last )
fulln( first="Bilal" , last="Haneef")
# ------------------*****************--------------------
# Function: dealing with an unknown number of arguments(Arbitrary number of arguments [*args] )
# in some cases we can not actually guess how many arguments user would pass when calling function 
# so we need a parameter that can take all values provided by the user
# as we dont know how many arguements would user pass we called these arguments arbitrary number of arguments
# here we see a parameter with(*),this parameter will deal with arbitrary numbers which convert all given arguments in tuple
def pizza( size , flavour , *toppings ): # according to convention we should write *args but its upto us
    print(f"You ordered for pizza of size {size} of flavour {flavour} with toppings {toppings} ")
pizza( 15 , "Beef" , "5 Onions" )
# now there are number of toppings onions , mushrooms , bacon , green pepper and many more
# what if user pass arguments for toppings more than 1 we have to use asterisk before that parameter which we know 
# would have more values
# those parameter which have this (*) store multiple values in form of tuples
pizza( 15 , "Beef" , "5 Onions" ,"6 Red pepper" , "4 mushrooms" )

def li_sum(*args):
    for a in args:
        print(a)
l1 = ([1,2,3],[3,4,5])
l2 = ([6,7,8],[9,10,11])
li_sum(*l1,*l2) # here i put *before l1 and l2 for tuple unpacking because my both list is in tuple  and i want each list in output which
# will unpack my tuple 
# *l1 = [1,2,3],[3,4,5]
# 
#  
# ------------------*****************--------------------
# Function: passing information back from them
# Functions only perform a given task when they are called
# but a functioon may also return value to user, the return value can be assigned, and be modified then
# return can return multiple values in form of tuple
# if we want to write more code in after return statment in functions body it will not be executed by interpretor 
# to utilize the value present in function we use return keyword so that it retuns value of that function and we can store that in value and use.
def sum( val1 , val2 ):
    ans= val1 + val2
    return ans , "Bilal" , 55   # we can convert it into list also by addning [] to it
result = sum(2,4) 
print(result)
# --------^^^--------
print(sum(2,4))
# ------------------*****************--------------------
# we can also use function as variable 
print("function as variables")
def add5(a,b):
    return a+b
def sub5(a,b):
    return a-b
result = add5(2,3) + sub5(2,3)
print(result)
# ------------------*****************--------------------
# Function: returning two values
def add_mult(num_1,num_2):
    add = num_1 + num_2
    mult = num_1 * num_2
    return add,mult # this will return tuple 
a = add_mult(2,5)
print(a)
# OR
b,c = add_mult(4,3) # we can also use values individually
print(b)
print(c)
########################################################
# Function: function returning function
def outerfunc():
    def innerfunc():
        print("Hello Pythonista")
    return innerfunc # notice: i didnt put braces here due to which the path of function will return to outer function and whenever i assign 
    # outerfunc in a variable and use print that variable output will be the path of function but when i use braces with that variable it will 
    # become function
var = outerfunc()
print(var) # this will print path of outerfunc
var() # this will print anything present in innerfunc
#########################################################
# Function: function inside function
def greater(a,b):
    if a>b:
        return a
    else:                   # this function will return greatest of two numbers
        return b
print(greater(9,20))

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>c:       # this function will return greatest of three numbers
        return b
    else:
        return c
print(greatest(2,4,9))
def new_greater(a,b,c):
    po = greater(a,b)       # this is function inside function
    return greater(po,c)
new_greater(1,9,50)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Funcction with all types of parameters
# sequence (PADK)
# 1. parameters
# 2. *args
# 3. defualt parameters
# 4. **kwargs
def func(name,*args,age="20",**kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)
func("Bilal",1,2,3,4,5,6,l_name = "Haneef",n_height = 13)
#########################################################
# Function: local variable Vs. global variable (this is called scope of a variable)
# local variable are the variable defined inside the function, their scope is only inside the function, they are not
# accessible outside the function
# global varialbes defined outsite the function and can be accessed and modified in and outside the function
def behappy():
    a = "Mr. Bean" # here "a" is a local variable
    # if we try to use the variable outside this func. it will generate error
    print(f"{a} is a very happy person")
behappy()
b = "Mr. B" # here "b" is a global variable
def sad():
    print(f"{b} is a sad person")
sad()
# by using globe keyword we can make a varibale global that can also be used outside function
# and Also, use the global keyword if you want to make a change to a global variable inside a function.
def fun():
    """ This is a fun function """
    global b
    b = input("Enter your name: ")
    print(f"Hello {b}")
fun()
# ------------------*****************--------------------
# a way to let user know more about function or to give information about function
# we use "DocString-document string" for this, inside function anything that we write in """ """ triple quotation is considered as docstr
# and to access docstr of a function, funcname.__doc__ this will show doc str of function
print(fun.__doc__)
# ------------------*****************--------------------
# Function within function
# we can call a function inside another function providing the required signauture of the function
def commissionCalc(sales):
    if sales>100:
        return sales*100
    elif sales>50:
        return sales*50
    elif sales>20:
        return sales*20
    else:
        return 0
def salCalc(basic,sales):
    grossSalary = basic + commissionCalc(sales)
    print(f"Your gross salary is {grossSalary}")
salCalc(2500,150)
salCalc(2500,500)
# ------------------*****************--------------------
# we have help function which helps us if we forgot something about any function's functionality
print(help(sum))