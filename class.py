# python is an object oriented programming language. This means that almost the code is implemented using a special
# construct called "Classes"
# programmers use class to keep related things togather. This is done using a keyword "class"  
# class is a blueprint(map) of anything     
# objects are instances of class means they are made by classes 
# object will follow class
# class contains attributes(variable) and behaviour(function)
# at first we define our attribute and at last we define our behaviour
# lets make a class which represents a person
# according to convention the first letter of class name will always capital
# in earlier versions of python we use parantheses with the class name 
print("                                     Person Class(Half")
class Person:
    def __init__(self,first_name,last_name,age): # __init__ method is called constructor
# we cannot define multiple init methods in class but if we do then the last init method will be considered as main init method
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
# the above class is not complete because we still have not defined the behaviour of this class
# lets create object
ps1 = Person("Bilal","Haneef",19) # that is object
ps2 = Person("Hamza","Haneef",25) # that is object
print(ps1.first_name)  
print(ps1.last_name) 
print(ps2.first_name) 
print(ps2.last_name) 
print(ps1.age) 
print(ps2.age) 
print(ps2.age)
# _______________________________________________________________________________________________________
# now lets continue to complete our class
# now if we want to make functions in our class just like list class has so many functions (pop,extend,insert,append..)
# know if i anyone want the full name of object we have to make a function 
print("                                     Person Class")
class Person:
    def __init__(self,first_name,last_name,caste,age):
        # we can change self to any name as our wish but its a convention to put self
        # here first_name which is attached with self is called instance variable and we use this name in objects
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.caste = caste
# ____________________________________________ INSTANCE METHODS / INSTANCE FUNCTIONS ________________________________________________________
# all the functions below called instance methods/functions which means i can use them in every instance/object of my class
    def full_name(self):
        return f"{self.first_name} {self.last_name} {self.caste} with {self.age}"
ps1 = Person("Bilal","Haneef","Qureshi",19) # that is object
ps2 = Person("Hamza","Haneef","Qureshi",25) # that is object
ps3 = Person("Ashraf","Jamal","Chudhry",45) # that is object
print(ps1.first_name) 
print(ps1.last_name) 
print(ps1.caste) 
print(ps1.age) 
print(ps2.first_name) 
print(ps2.last_name)
print(ps2.caste) 
print(ps2.age) 
print(ps3.first_name) 
print(ps3.last_name)
print(ps3.caste) 
print(ps3.age) 
print(Person.full_name(ps1))
print(ps1.full_name()) # another way
print(Person.full_name(ps2))
print(ps2.full_name()) # another way
print(Person.full_name(ps3))
print(ps3.full_name()) # another way
# now how to change the value of an attribute 
ps2.first_name = "Zeeshan"
print(ps2.first_name)
print(ps2.full_name())
print(Person.full_name(ps2))
# _______________________________________________________________________________________________________
print("                                     Cirle Class")
class Circle:
    pi = 3.141 # class variable 
# for each objecct/instance of my class , class variable will be same
# we declare class variable to use in class and we can also change its value outside the class thorugh this 
# syntax- classname.class_var = value
# ____________________________________________ INSTANCE METHODS / INSTANCE FUNCTIONS ________________________________________________________
# all the functions below called instance methods/functions which means i can use them in every instance/object of my class
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        # Area = Pi*r**2
        return (Circle.pi)*(self.radius**2)
    def circumferencce(self):
        # circumference = 2*pi*r
        return 2*(Circle.pi)*(self.radius)

print(Circle.pi)
ok = Circle(4)
ok1 = Circle(6)
print(Circle.area(ok))
print(Circle.circumferencce(ok))
# _______________________________________________________________________________________________________
print("                                     Calculator Class")
class Calculator:
    def __init__(self,f_num,s_num):
        self.f_num = f_num
        self.s_num = s_num
# ____________________________________________ INSTANCE METHODS / INSTANCE FUNCTIONS ________________________________________________________
# all the functions below called instance methods/functions which means i can use them in every instance/object of my class.
    def addition(self):
        return self.f_num + self.s_num
    def product(self):
        return self.f_num * self.s_num
    def subtraction(self):
        return self.f_num - self.s_num
    def int_division(self):
            if self.s_num != 0:
                return self.f_num // self.s_num
            else:
                return "You have entered 0 for denominator"
    def float_division(self):
        if self.s_num != 0:
            return self.f_num / self.s_num
        else:
            return "You have entered 0 for denominator"
o1 = Calculator(5,5)
o2 = Calculator(2,5)
o3 = Calculator(3,5)
b = o3.int_division()
print(b)
o4 = Calculator(2,2)
print(o4.subtraction())
o5 = Calculator(9,6)
o6 = Calculator(2,0)
print(o6.int_division())
print(o1.float_division())
# _______________________________________________________________________________________________________
print("                                     Laptop Class")
class Laptop:
    disc_rate = 10 # here i fixed my discount at 10% on every laptop 
    def __init__(self,name,price,model):
        # attributes or instance varaible
        self.name = name
        self.price = price
        self.model = model
    def discount(self): # 50000*(40/100)
        a = (Laptop.disc_rate)/100 # if we know that in future our class value gonna be changed so we put self.classvar instead classname.class_var
        b = (self.price)*(a)
        disco = (self.price)-(b)
        return disco
obj1 = Laptop("EB",50000,"HP")
obj2 = Laptop("CB",10000,"Google")
obj3 = Laptop("Apple Book",90000,"Apple")
Laptop.disc_rate = 0 # here i change by 10% discount to 0% and i can change it for any object individually by this synrax - obj_name.class_var = value
print(obj1.discount())
print(obj2.discount())
print(obj3.discount())
#  here __dict__ is called data discriptor
print(obj1.__dict__) # __dict__ convert any object's argument to dictionary in which keys are parameters and values are argument
# now im gonna change the disc_rate for obj3 so when i change class variable for a particular object it will add that variable as instance
# variable in our object
print(obj3.__dict__,"before changing disc_rate")
obj3.disc_rate = 30
print(obj3.__dict__,"after changing disc_rate")
print(obj3.discount()) # now this will not show my changed discount until i changed the Laptop.disc_rate to self.disc_rate 
# _______________________________________________________________________________________________________
# this class will tell us how many instances have been created
print("                                     Class Teacher")
class Teacher:
    ins_count = 0
    def __init__(self,T_name,T_subject,T_experience):
        Teacher.ins_count += 1
        self.ob_count_str = "You have created " + str(Teacher.ins_count) + " instances of Teacher Class"
        self.T_name = T_name
        self.T_subject = T_subject
        self.T_experience = T_experience
objt1 = Teacher("Sir Shahab","ISE",45)
objt2 = Teacher("Sir Badar","ICS",30)
objt3 = Teacher("Miss Shahnaz","ISL",25)
objt4 = Teacher("Miss Maleeha","CLD",10)
objt5 = Teacher("Miss Huma","ISE_lab",5)
objt6 = Teacher("Miss Erum","ENG",54)

print(Teacher.ins_count)
print(objt6.ob_count_str)
# __________________________________________ CLASS METHODS _____________________________________________________________
# A class method is a method which is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
# It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that 
# will be applicable to all the instances.
# so here we want to define class method in our class Teacher that works same as instance variable ob_count_str
class Person:
    age = 25
    def printAge(cls):
        return f"The age is:, {cls.age}"
# create printAge class method
Person.printAge = classmethod(Person.printAge)
print(Person.printAge())
# When do we use class method?
# 1. Factory methods
# Factory methods are those methods which return a class obje ct (like constructor) for different use cases.


print("                                     Class Teacher1")
class Teacher1:
    ins_count = 0
    def __init__(self,T_name,T_subject,T_experience):
        Teacher1.ins_count += 1
        self.T_name = T_name
        self.T_subject = T_subject
        self.T_experience = T_experience
# in instance method first parameter is instance iteself(which is self) but in class methods, first paremeter will be class it self
# so for this purpose, python has predefined decoartor (@classemthod) which we attach with our class method by syntactic sugar
    @classmethod
    def counting_ins(cls): # class method takes its first parameters it self, therefore i put "cls" here , and acc. to convention we always 
# have to put cls as class parameter we can change it as our wish but its a convention to put cls here
        return f"You have created {cls.ins_count} instances of class {cls.__name__}" # to print name of class function we have to use classname.__name__
# above i can also use my class var as Teacher1.ins_count but here "cls" is now reperesenting our class thats why i put cls there  
    def full_intro(self):
        return f"{self.T_name} teaches {self.T_subject} and has {self.T_experience} years of experience"

obj1 = Teacher1("Sir Shahab","ISE",45)
obj2 = Teacher1("Sir Badar","ICS",30)
obj3 = Teacher1("Miss Shahnaz","ISL",25)
obj4 = Teacher1("Miss Maleeha","CLD",10)
obj5 = Teacher1("Miss Huma","ISE_lab",5)
obj6 = Teacher1("Miss Erum","ENG",54)
print(obj2.full_intro())
# we always need to use class method by using class name | classname.classmethod()
print(Teacher1.counting_ins()) 
print(obj5.counting_ins()) # we can use this method also but thats not the good way of using class method 
# in line 207 whats hapenning is when interpretor execute this line it will check that is counting_ins a instance method which counting_ins not
# after which it will check that is counting_ins a class method and yes it is so this will return the result
# ______________________________________________ CLASS METHODS AS CONSTRUCTOR  _________________________________________________________________
# in the above class teacher1 if i want to make object like this , obj = Teacher1("Sir Badar,ICS,20") for this i need to use class method as 
# constructor
print("                                     Class Teacher2")
class Teacher2:
    def __init__(self,T_name,T_subject,T_experience):
        self.T_name = T_name
        self.T_subject = T_subject
        self.T_experience = T_experience
# here i will define my class method which acts as constructor
    @classmethod
    def instance_creater(cls,string):
        name,subject,experience = string.split(",") # this will split user input and save into individual variables
        return cls(name,subject,experience)
    def full_intro(self):
        return f"{self.T_name} teaches {self.T_subject} and has {self.T_experience} years of experience"
ob1 = Teacher2.instance_creater("Sir Badar,ICS,20")
print(ob1.full_intro())
# _____________________________________________________ STATIC METHOD IN CLASS ________________________________________________________________
# A static method is also a method which is bound to the class and not the object of the class.
# A static method can’t access or modify class state.
# It is present in a class because it makes sense for the method to be present in class.
# __________OR__________
# static methods are used when some processing is related to the class but does not  need the class or its instances to perform any work
# we use static method when we want to pass some values from outside and perform some action in the method
# @staticmethod need to write above the static method
print("                                     Class Teacher3")
class Teacher3:
    def __init__(self,T_name,T_subject,T_experience):
        self.T_name = T_name
        self.T_subject = T_subject
        self.T_experience = T_experience
# here i will define my class method which acts as constructor
    @staticmethod
    def name():
        return "Static method get called"
    @staticmethod
    def mobile(model,price):
        return f"{model} costs {price} "
    @classmethod
    def instance_creater(cls,string):
        name,subject,experience = string.split(",") # this will split user input and save into individual variables
        return cls(name,subject,experience)
    def full_intro(self):
        return f"{self.T_name} teaches {self.T_subject} and has {self.T_experience} years of experience"
print(Teacher3.name())
print(Teacher3.mobile("Xiaomi note 8",29000))
# _____________________________________________   ENCAPSULATION _______________________________________________________________
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and 
# the methods that work on data within one unit.
# _____OR______
# to keep data(instance var/class var etc) and function/method(instance method,static method ,class method ) together like we put them in a
# capsule, this is called encapsulation
# 
# Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, finance section, sales
#  section etc. The finance section handles all the financial transactions and keeps records of all the data related to finance. Similarly, 
# \the sales section handles all the sales-related activities and keeps records of all the sales. Now there may arise a situation when for
#  some reason an official from the finance section needs all the data about sales in a particular month. In this case, he is not allowed 
# to directly access the data of the sales section. He will first have to contact some other officer in the sales section and then request
#  him to give the particular data. This is what encapsulation is 

# ________________________________________________________  ABSTRACTION _______________________________________________________________
# Abstraction means hiding the complexity and only showing the essential features of the object. So in a way, Abstraction means hiding the
#  real implementation and we, as a user, knowing only how to use it.

# Real world example would be a vehicle which we drive with out caring or knowing what all is going underneath.
# A TV set where we enjoy programs with out knowing the inner details of how TV works.

# ________________________________________________________  NAMING CONVENTION _______________________________________________________________
# in other programming languages like c++ , java there are privet methods , privet variables or public things
# but in python every thing is public so if i want to make anything privet to other developers i have to put single underscore before it (_name)
# now my name variable is privet here so that no one can change it. putting underscore doesnt mean that user can't able to change the function/var
# but it lets developer known that you dont need to touch it and putting underscore is just a convention
# anything with double underscore __name__ is called "double undersore" or "dunder methods" or "magic methods"
class Phone:
    def __init__(self,name,model,price):
        self.name =  name
        self.model = model
        self._price = price # so here if i put _ before price that attached with self after which it will let me change the value of price 
        # outsite my class 
    def fullname(self):
        return self.name + self.model
    
p1 = Phone("Nokia","3310",50000)
p1._price = 900000
print(p1._price)
p2 = Phone("Sony erecson","note 8",20000)

# ________________________________________________________  NAME MANGLING _______________________________________________________________
# so in the above paragraph of name convention putting single undersore means something is privet but we can also change the value so how to 
# prevent other developers changing the value.
# for this purspose we use double underscore before the name of variable or function etc. which will prevent others to change the value
print("                                    Phone1")
class Phone1:
    def __init__(self,name,model,price):
        self.name =  name
        self.model = model
        self.__price = price # so here if i put __ before price that attached with self after which it wont let me change the value of price 
        # outsite my class 
    def fullname(self):
        return self.name + self.model
    
po1 = Phone1("Nokia","3310",50000)
# po1.__price = 900000
# print(po1.__price) # this will generate error that 'Phone1' object has no attribute '_price' , just because we have changed the instance var
#   by putting double underscore 
print(po1.__dict__)
# so what python did here is it has changed the __price to _Phone1__price which will prevent us to change the value
print(po1._Phone1__price) # so this will print my actual price of phone
# we can also change the value of it now
po1._Phone1__price = 10000
print(po1._Phone1__price)
print(po1.__dict__)
# ________________________________________  PROPERTY(SETTER AND GETTER) DECORATOR __________________________________________________________
print("                                         Smartphone")
class Smartphone:
    def __init__(self,brand,model_name,price):
        self.brand =  brand
        self.model_name = model_name
        if price > 0:
            self._price = price
        else: 
            self._price = 0
# we can also do this,  
#       self._price = max(price,0)
        self.total_specification = f"{self.brand} {self.model_name} {self._price}"
    def make_a_call(self,number):
        return f"calling {number}"
    def fullname(self):
        return self.brand + " " + self.model_name
    @property
    def specification(self):
        return f"{self.brand} {self.model_name} {self._price}"
        
p1 = Smartphone("Nokia","3310",50000)
# print(p1._price)
# so there are some problems in this class that we need to care about.
# first is what if someone makes an object in which price of smartphone is a negative number, since price cannot be negative so we have to 
# tackle this(see code changes in line line no 347)
p2 = Smartphone("Nokia","3310",-9000)
print(p2._price) 
# second problem is if i change the value of instance variable(price) then the change wont appear in total specification(the reason behind this
# is that when we make our object our init method get called and creates our instance variable total_specification and when we change the value
# of price it will not appear in our total_spec b/c it has alredy created )
# solution to this problem will be that we can make a function for total_specification
p2._price = -943000
print(p2._price,"changed price") 
print(p2.total_specification)
# print(p2.specification())  
# here comes property decorator , if i use property decorator(in line no 358) for my specification function , which let me use my specification
#  function as an attribute or instace variable instead like function 
print(p2.specification)  

print("                                         Smartphone1")
class Smartphone1:
    def __init__(self,brand,model_name,price):
        self.brand =  brand
        self.model_name = model_name
        if price > 0:
            self._price = price
        else: 
            self._price = 0
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,n_price):
        self._price = max(n_price+1,0)
    def make_a_call(self,number):
        return f"calling {number}"
    def fullname(self):
        return self.brand + " " + self.model_name
    @property
    def specification(self):
        return f"{self.brand} {self.model_name} {self._price}"

sp1 = Smartphone1("Nokia","3310",50000)
sp2 = Smartphone1("Nokia","3310",9000)
print(sp2._price,"original price")
sp2.price = 700000
print(sp2.price,"changed price") 
print(sp2.specification)  
print(sp2.price)
print(sp2.__dict__)

# now there is a problem if i change the value of price to negative(in line # 402) it will let this happen instead i want to set the value
# to 0. 
# for this purpose we can use setter and getter decorator 
# now we want to set value for price so here we use setter decorator which is actually property decorator it-self , which we define in 
# line # 390
# now to set value of price so that it can not be negative , i have to define me setter in line no (393) , always make setter after
#  getter(property) decorator elsewise this will give error
