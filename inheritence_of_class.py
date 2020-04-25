class Phone: # parent class / base class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
    def make_a_call(self,p_number):
        return f"calling {p_number} ........"
    def fullname(self):
        return f"{self.brand} {self.model_name}"
# above i have my class that have brand,model_name and price as instance variable
# below i have my class that also have brand,model_name and price as instance variable and some other instance variable as 
# well
# but if i already have brand,model_name and price as instance variable in my class Phone so why do i need to create them
# again which shows im not following DRY(don't repeat yourself) rule/principle of programming

# class Smartphone:
#         def __init__(self,brand,model_name,price,ram,internal_m,rare_cam):
#             self.brand = brand
#             self.model_name = model_name
#             self._price = max(price,0)
#             self.ram = ram
#             self.internal_m = internal_m
#             self.rare_cam = rare_cam
#         def make_a_call(self,p_number):
#             return f"calling {p_number} ........"
#         def fullname(self):
#             return f"{self.brand} {self.model_name}"
# for this purpose inheritence comes into play by which i dont need to create those instace variable and functions/methods
# that are already defined in other class
#                                             ______OR______
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# first method to inherit class is, (uncommon method/way)
# to use Phone class' funcctions in Smartphone class i need to pass my class Phone in Smartphone braces(thats why i have 
# removed my functions(functions that present on line # 24 and 26 ) from Smartphone class which are already defined in my Phone class )
# to use Phone class' variable in Smartphone class i need to pass all my instance variables(of Phone class) in init method
# that attached to my Phone(under main init method) (thats why i have removed my instace variable(line # ) from Smartphone 
# class which are already defined in my Phone class )
# syntax - to use Phone class' variable in smartphone class  [ classname.__init__(self,inst_var,inst_var,inst_var,..) ]

print("                                                           Uncommon way")
class Smartphone(Phone): # derived class / child class
    def __init__(self,brand,model_name,price,ram,internal_m,rare_cam):
        Phone.__init__(self,brand,model_name,price)
        self.ram = ram
        self.internal_m = internal_m
        self.rare_cam = rare_cam
    def memory_cam(self):
        return f"Ram is {self.ram} , internal memory {self.internal_m} and rare camera is {self.rare_cam}"
    
ob1 = Smartphone("Xioami","Redmi Note 8",29000,"8 GB","16 GB","40 MP")
ob2 = Smartphone("OnePlus","Note 8",50000,"12 GB","21 GB","90 MP")

print(ob2.make_a_call(4220107239559))
print(f"{ob1.fullname()} and price is {ob1._price}")


# second method to inherit class is,
# to use Phone class' funcctions in Smartphone class i need to pass my class Phone in Smartphone braces(thats why i have 
# removed my functions(line # ) from Smartphone class which are already defined in my Phone class )
# to use Phone class' variable in Smartphone class i need to pass all my instance variables(of Phone class) in init method
# that attached to my super function(under main init method) and in this init method we dont need to pass self as first 
# parameter
# syntax - to use Phone class' variable in smartphone class  [ super().__init__(inst_var,inst_var,inst_var,..) ]

print("                                                           Common way")
class Smartphone1(Phone): # derived class / child class
    def __init__(self,brand,model_name,price,ram,internal_m,rare_cam):
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_m = internal_m
        self.rare_cam = rare_cam
    
ob1 = Smartphone1("Xioami","Redmi Note 8",29000,"8 GB","16 GB","40 MP")
ob2 = Smartphone1("OnePlus","Note 8",50000,"12 GB","21 GB","90 MP")

print(ob2.make_a_call(4220107239559))
print(f"{ob1.fullname()} and price is {ob1._price}")
# _____________________________________________________________________________________________________________________________________________
class PhoneOne: # parent class / base class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
    def make_a_call(self,p_number):
        return f"calling {p_number} ........"
    def fullname(self):
        return f"{self.brand} {self.model_name}"
class PhoneTwo: # parent class / base class
    def __init__(self,glass,secondary_mic,primary_mic):
        self.glass = glass
        self.secondary_mic = secondary_mic
        self.primary_mic = primary_mic
    def comp_spec(self):
        return f"{self.glass} , {self.primary_mic} and {self.secondary_mic}"
    def features(self):
        return f"Secondary mix {self.secondary_mic} and primary mic {self.primary_mic}"

class Smartphone_One(PhoneOne,PhoneTwo): # derived class / child class
    def __init__(self,brand,model_name,price,glass,secondary_mic,primary_mic,ram,internal_m,rare_cam):
        PhoneOne.__init__(self,brand,model_name,price)
        PhoneTwo.__init__(self,glass,secondary_mic,primary_mic)
        self.ram = ram
        self.internal_m = internal_m
        self.rare_cam = rare_cam
    
object1 = Smartphone_One("Xioami","Redmi Note 8",29000,"Gorilla Glass","No","Yes","8 GB","16 GB","40 MP")
object2 = Smartphone_One("OnePlus","Note 8",50000,"Non-Gorilla Glass","Yes","Yes","12 GB","21 GB","90 MP")

print(object2.make_a_call(4220107239559))
print(f"{ob1.fullname()} and price is {ob1._price}")
print(object2.primary_mic)
print(object2.features())
print(object2.comp_spec())
# ___________________________________________________________ MULTILEVEL INHERITANCE ___________________________________________________________ 
# Q. Can we inherit a class in multiple classes?
# A. Yes, we can inherit a class as many times as we want.
# Q. Can we inherit a class that has already inherited a class?
# A. A class can be derived from more than one base classes in Python. This is called multilevel inheritance

# so in line # 67 i have a class named Smartphone in which i inhetrit Phone class , now im going to inherit Smartphone class in the class below
print("                                         Multilevel Inheritance")
class Exp_Smartphone(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_m,rare_cam,front_cam):
        super().__init__(brand,model_name,price,ram,internal_m,rare_cam)
        self.front_cam = front_cam
    def cameras(self):
        return f"Rare camera is {self.rare_cam} and front camera is {self.front_cam}"

objec1 = Exp_Smartphone("Xioami","Redmi Note 8",29000,"8 GB","16 GB","40 MP","8 MP")
objec2 = Exp_Smartphone("OnePlus","Note 8",50000,"12 GB","21 GB","90 MP","13 MP")
print(objec1.cameras())
print(objec2.fullname())
print(objec2.make_a_call(4220107239559))
print(objec1.memory_cam())
# ____________________________________________________________ MRO(METHOD RESOLUTION ORDER) ____________________________________________________________
# MRO is the order in which python search our methods of class and its instance variable
# syntax - help(classname)
# e.g if i want to see the MRO of class Smartphone, i do this
print(help(Smartphone))
# here in line # 135 i have called fullname func  from Smartphone class' object , what python do is ,  it will check my MRO so first we have 
# smartphone class in mro, from where fullname doesnt belong so next class in mro is phone , in which we have defined fullname func so thats
# how mro helps us 
print(help(Exp_Smartphone))
# _________________________________________________________ METHOD OVERIDE ____________________________________________________________
# in my phone class i have fullname func that returns brand and model name of obj , so if want fullname to print something else , what i do is
# i again make fullname function in my Exp_Smartphone class which will return brand , model name as well as price 
# whenever i call my function fullname mro checks it in every class but i have this method in both classes(Exp_Smartphone and Phone) so what 
# python do is it will return this method from whatever class it found first.
# first it will search in Exp_Smartphone and we already defined this method in this class so it will return this and stop searching in other 
# classes thats the reason why its not printing fulllame of Phone class because it overides now.
# __________________________________________________isinstance and issubclass funcions _______________________________________________________
# ____________________________________________________________ isinstance() ____________________________________________________________
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
# syntax - isinstance(object, type)
# object	Required. An object.
# type	A type or a class, or a tuple of types and/or classes
print(isinstance(objec1,Exp_Smartphone)) # so object belongs to exp_sp class, this will return True

# Check if "Hello" is one of the types described in the type parameter:
print(isinstance("Hello", (float, int, str, list, dict, tuple)))
print(isinstance([1,2,3,4,4,5,6], (float, int, str, list, dict, tuple)))
print(isinstance([1,2,3,4,4,5,6], (float, int, str, dict, tuple)))

# ____________________________________________________________ issubclass() ____________________________________________________________
# The issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False.
# syntax - issubclass(object, subclass)
# object	Required. An object.
# subclass	A class object, or a tuple of class objects
print(issubclass(Smartphone,Phone)) # this will return True because Smartphone clas is a subclass of Phone class
print(issubclass(Phone,Smartphone))