a=10
# 'a' is a variable name called "Identifier"
# '=' is a assignment operator
# '10'  is integer value
# line no 1 is reads as "intger value 10 is assigns to a varaible a"
print(a)
print(type(a))
#       --------------------*************************-------------------------
# now we assign a new value to a variable 'a'
a=80.18
print(a) # here what happend is the integer value which we have assigned to variable 'a' prior is overwrite by 
# floating value due to which print function prints float point value.
# in python the variable is independent of type(int,char,float etc) interpreter automatically identifies the type of
# variable. Precisely, we dont have to define data type in python.
print(type(a))
#       --------------------*************************-------------------------
a="Bilal"
print(a)
print(type(a))
#       --------------------*************************-------------------------
#                                  Concatenation
student_name= "Bilal"
father_name= "\tHaneef"
print(student_name  +  father_name) # this is called "String Concatenation"
#  in string '+' is not addition but it is concatenation
a="2"
b="2"
print(a+b)
#       --------------------*************************-------------------------
num_1=80
num_2=0.18
sum=num_1 + num_2
print(sum)
#       --------------------*************************-------------------------
#                             Mathematical  Operator
print(10+100)
a=1
b=2
print(a+b)
# ---------------
print(a-b)
#---------
print(a*b)
#  ------------
print(a/b)
print(b/a) # by default python gives float point value. single slash gives float division
print(b//a) # //double slash gives integer division 
# -------------
a=1000
b=10.50
print(a-b)
#  --------------------***************************----------------
name , age = "Bilal", 24
print("your name is " + name + "and age is" + age)