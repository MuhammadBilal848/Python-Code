name="Bilal"
age="19"
print("Hello " + name + " your age is " + age )
 # the above in python takes as ugly syntax
#  ---------------**********************--------------
 # we can use string formatting of python 3 or python 3.6
 # string formatting in python 3
name="Bilal"
age=19
print("Hello {} your age is {}".format(name,age))
# the code above(9) is used in python 3 for string formatting
# the place holder "{}" used above indicate the variable position and the format method used to let interpretor know 
# which variable we want to use first. The format method is independent of string or integer value.
#  ---------------**********************--------------
name="Bilal"
age=19
print(f"Hello {name} your age is {age}")
# dont forget to use "f" before quotes
# the above code(17) is called clean syntax.