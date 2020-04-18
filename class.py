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
# so here we want to define class method in our class Teacher that works same as instance variable ob_count_str
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
        return f"You have created {cls.ins_count} instances of class Teacher1"
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
