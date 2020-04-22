# if we want to track position of our item in iterable we use enumerate function
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.
# syntax - enumerate(iterable, start)
# iterable - An iterable object
# start - A Number. Defining the start number of the enumerate object. Default 0
# first we take e.g. of this without enumerate func. 
print("                                     enumerate()")
a = ["a","ab","abc","abcd"]
pos = 0
for b in a:
    print(f"{pos} -----------------> {b}")
    pos += 1
# above code will track position of our items 
# now we make this using enumerate function
l = ["a","ab","abc","abcd"]
for  o,p in enumerate(l): # hhere
    print(f"{o} --------------------> {p}")
# now we define a function that will take two arguments first is list containing names and second is the name which we want to check is present
# in our list or not if name is present then function will return its index number it its not present function will return -1
def kom(l,name): 
    for pos,b in enumerate(l):
        if b==name:
            return pos
    return -1
a = kom(["Abuzar","Bilal","Usama","Nofil","Zaigham"],"Zaigham")
print(a)
c = kom(["Abuzar","Bilal","Usama","Nofil","Zaigham"],"Araib")
print(c)
# ______________________________________________________________________________________________________________________________________________
# The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
# syntax - map(function, iterables)
# function	Required. The function to execute for each item
# iterable	Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function 
# has one parameter for each iterable.
print("                                     map()")
a = [1,2,3,4,5,6,7,8,9]
def square(num):
    return num**2
b = map(square,a) # at this time map objects is stored in our var a but not list so if we convert it in to tuple,list then it will show it.
# map functions takes two parameter first is "func" means which function's operation we want to apply on our
# next parameter named "*iterable(which is *args)"
# for e.g. i have a list[1,2,3,4,5,6,7,8,9] and i want another list in each number converted into its square
# so for this what i do is that i make a function that takes a number as parameter and return its square
# so i give map function its first parameter which is sqaure and in next parameter i will give my list
print(b) 
m = list(map(square,a))
print(m,"squares by simple function")
# we can also do this with the help of lambda function
a = [1,2,3,4,5,6,7,8,9]
d = list(map(lambda n : n**2,a))
print(d,"square by lambda function")
# some more examlpe of map function
l = ["abc","abcd","abcde","abcdef"]
k = list(map(lambda b : len(b),l))
print(k)
# _____________________OR__________________
l = ["abc","abcd","abcde","abcdef"]
u = list(map(len,l)) # we can iterate to this list as many times as we want 
print(u)
u1 = map(len,l)
print(u1) # this will print map object which is iterable(means i can loop on it only one time )
for q in u1:
    print(q)
# now im gonna loop again to map object but it will not let me do it(it wont show any error but it prints nothhing on screen)
for v in u1:
    print(v)
# loop = list(map(int,input().strip()   .split())) # this is to take input from user and convert all its given numbers in integers and make a list of 'em
# print(loop)
# function below works just like map funtion 
for a in map(lambda n : n**2 , [1,2,3,4,5,6,7,8,9]):  # in this way i can iterate as many times as i want
    print(a)                                            
for a in map(lambda n : n**2 , [1,2,3,4,5,6,7,8,9]):
    print(a)

def square(a):
    return a**2
def special_sq(func,l):
    new_l = []
    for a in l:
        new_l.append(func(a))
    print(new_l)
special_sq(square,[1,2,3,4,5,6])
# ______________________________________________________________________________________________________________________________________________
#  The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
# syntax - filter(function, iterable)
# function 	A Function to be run for each item in the iterable(thorugh which filter func passes each value of iterable and check it is acceptable
# or not)
# iterable	The iterable to be filtered

print("                                     filter()")
def is_even(a):
    return a%2==0
numbers = [1,2,3,4,5,6,7,8,9,10]
d = list(filter(is_even,numbers)) # now filter function filters every object of iterable(numbers) thorugh the function and obviously only even
print(d) # numbers can make condition True
c = filter(is_even,numbers) # this will return filter object and i can iterate over this one time just as map object
for a in c:
    print(a)
# but if i convert filter object into tulpe,list so in this way i can iterate as many times as i want
for b in d:
    print(b)
for b in d:
    print(b)

def filt_name(*args):
    for item in args:
        if item==str(item):
            return True
        else: 
            return False
b = list(filter(filt_name,["Usama","Abuzar",12,"nofil",23,"z",4,"KK"]))
print(b)

fill = list(filter(lambda name : True if (name is str(name)) else False,["Usama","Abuzar",12,"nofil",23,"z",4,"KK"]))
print(fill)

# function that filters vowels 
def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False  
# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
# using filter function 
filtered = filter(fun, sequence) 
print('The filtered letters are:') 
for s in filtered: 
    print(s) 
# ___________________________________________________ DIFFERENCE BETWEEN MAP AND FILTER ___________________________________________________ 
print("                                       map() Vs filter()")
# Map takes all objects in a list and allows you to apply a function to it.
a = [1,2,3,4,5,6,7,8,9]
sq = list(map(lambda v : v*2 , range(0,10)))
print(sq)   
# Filter takes all objects in a list and runs that through a function to create a new list with all objects that and check whether it is accepted
# for that function or not if it is then it will print that number and if it is not it will not print this number.
# filter function just check our object that it is accepted for that function or not.
a = [1,2,3,4,5,6,7,8,9]
sq = list(filter(lambda v : v*2 , range(0,10)))
print(sq)
# map()
numbers = [1,2,3,4,5,6,7,8,9,10]
def is_even(a):
    return a%2==0
d = list(map(is_even,numbers)) # Here map has checked the condition applied on the element one by one and passed a boolean output.
print(d)
#  filter()
numbers = [1,2,3,4,5,6,7,8,9,10]
def is_even(a):
    return a%2==0
f = list(filter(is_even,numbers))
print(f)
# ______________________________________________________________________________________________________________________________________________
# The iter() function returns an iterator object.
# syntax - iter(object, sentinel)
# object	Required. An iterable object
# sentinel	Optional. If the object is a callable object the iteration will stop when the returned value is the same as the sentinel

print("                                      iter()")
a = [1,2,3,4,5,6] # ----------------> iterable    (something that can be looped over)
iterable = iter(a)
print(iterable) # this will return a list_iterator object which is iterator
# now this iter function takes each element of my list one by one and assign in my iterable varibale and if i want to access those element every 
# time i use next function that returns the next item in an iterator.
print(next(iterable))
print(next(iterable))
print(next(iterable)) 
print(next(iterable))
print(next(iterable))
print(next(iterable)) # this is my last element from a list
# print(next(iterable)) # now my list is empty or has no element in it, this will give error 
# Thats how for loop works
# whenever iter() and next() applied on an object(list,tuple,string,etc), this object is called iterable 
# or anything on which we can apply for loop is called iterable
# ______________________________________________________________________________________________________________________________________________
# The next() function returns the next item in an iterator.
# You can add a default return value, to return if the iterable has reached to its end.
# this has two parameters first is iterator and second is default(If default is given and the iterator is run of values, it is returned instead
#  of raising StopIteration)
print("                                      next()")
a = map(lambda sq : sq**2 , range(1,10)) 
print(a) # so this is map object which is an iterator itself 
# so i can direct apply next function to it and get all my values
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a,"stop iteration"))
# line no 123 is also a iterator and i can iterate over it by next func.
# ______________________________________________________________________________________________________________________________________________
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
# syntax - zip(iterator1, iterator2, iterator3 ...)
# iterator1, iterator2, iterator3 ...	Iterator objects that will be joined together
print("                                     zip()")
User_ID = ["user 1" , "user 2" , "user 3"]
User_NAME = ["Bilal","Hamza","Zeeshan"]
# so if we want to zip this use we use zip funtion
b = zip(User_ID,User_NAME) # this will return zip object we have to change the object to list or tuple, i can pass as many iterable as i want
print(b)
a = list(zip(User_ID,User_NAME))
print(a) # now at this point i have a pair of user name and user id and if i want to convert it into dictionary i can use dict function
print(dict(a),"dictionary")
for e in b: # i can also iterate through my zip object but only one time but with tuple and list i can iterate as many times as i wannt
    print(e)
# $$$$$$$$$$$$$$$$$$
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l = [ (1,2) , (3,4) , (5,6) , (7,8) ] # now i want to unzip this or unpack this into l1 and l2 so this is what i do
l = [ (1,2) , (3,4) , (5,6) , (7,8) ]
l1,l2 = list(zip(*l)) # this (*) will unzip or unpack my list into two tuples and i can store both in individual variable
l1 = list(l1)
l2 = list(l2)
print(l1)
print(l2)

l = [ (1,2) , (3,4) , (5,6) , (7,8) ]
for a in l:
    print(max(a))
# _________OR__________
for k in zip(l1,l2,):
    print(max(k))

# define a function that takes multiple list containing numbers [1,2,3] , [4,5,6] , [7,8,9] and return average (1+4+7)/3 ,(2+5+8)/3,(3+6+9)/3
def average(*args):
    new_avg = []
    for pair in zip(*args):
        new_avg.append(sum(pair)/len(pair))
    print(new_avg)
average([1,2,3] , [4,5,6] , [7,8,9])
# now we make the same function using lambda expression
lam_average = lambda *args : [ sum(pair)/len(pair) for pair in zip(*args) ]
print(lam_average([1,2,3] , [4,5,6] , [7,8,9]))
# ______________________________________________________________________________________________________________________________________________
# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.
# syntax - all(iterable)
# iterable : An iterable object (list, tuple, dictionary)
print("                                      all()")
a = [0,1,0,1,1,0] # so here list contain binary digit which acts as True and False so all function return False bc not all elements are True in
# list
print(all(a))

a = [1,1,1,1,1,1,1] # now all elements are True
print(all(a))

mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)
print(x)

mydict = {1 : "Apple", 1 : "Orange"}
x = all(mydict)
print(x)

# so now define a list comprehension that return True if all numbers in list are even else False and after which we have to check the.com list of 
# True and False that all elemets in the list are True or False
l = [2,4,6,8,10]
a = [ b%2==0 for b in l ]
print(a)
print(all(a)) # this will return True because my list(l) contain all even numbers

l = list(range(1,11))
a = [ b%2==0 for b in l ]
print(a)
print(all(a))  # this will return False because my list contain both even and odd numbers

def addi(*args):
    total = 0
    for a in args:
        total += a
    return total
print(addi(1,9)) # what if user passes any kind of string or list or tuple as argument so program will generate ereor, to prevent this we can
# use all function

def addit(*args):
    a = [ True if (type(b) is int) else False for b in args ]
    if all(a):
        total = 0
        for a in args:
            total += a
        return total
    else: 
        return "you have entered wrong data type"
print(addit(1,2,3,4,5,1))
print(addit(1,2,3,"bilal",[1,2,3]))

# ______________________________________________________________________________________________________________________________________________
# The any() function returns True if any item in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the any() function will return False.
# syntax - any(iterable)
# iterable	An iterable object (list, tuple, dictionary)
print("                                      any()")
a = [1,0,0,0,0,0] # so here only one number is 1 and rest of them are 0 , so any function returns True because there is 1 present in list
print(any(a))

a = [0,0,0,0,0,0] # so here all elements are 0 therefore any function returns False
print(any(a))

mydict = {1 : "Apple", 1 : "Orange"}
x = all(mydict)
print(x)

mydict = {0 : "Apple", 0 : "Orange"}
x = all(mydict)
print(x)
# ______________________________________________________________________________________________________________________________________________
# The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.
# If the values are strings, an alphabetically comparison is done.
# syntax - min(*iterable, default=obj, key=func) 
# default (optional) - default value if the given iterable is empty  g = mix([],default=9) here my iterable is empty and default set to 9 so 
# function will return 9
# key (optional) - key function where the iterables are passed and comparison is performed based on its return value ( key = value )


# n1, n2, n3, ...	One or more items to compare
print("                                      min()")
a = [1,2,3,4,5]
print(min(a))

print(min(0.0001,0.01,1,2,3,4,5,6,7,8,999,999999))

a = ["Bilal","Hamza","Abuzar"]
print(min(a))

# now if we want min function to work like that if i pass an iterable in min function so min function return the shortest string in iterable
# for this purppose i need to make a function that takes item and return its length
def len_item(item):
    return len(item)

a = ["Bill","Abuzar","Harison","Barry"] 
print(min(a, key = len_item))  # now here i can use that function len_item in key //// we  can also use lambda expression as value against key

# ______________________________________________________________________________________________________________________________________________
# The max() function returns the item with the highest value, or the item with the highest value in an iterable.
# If the values are strings, an alphabetically comparison is done.
# syntax - max(*iterable, default=obj, key=func) 
# default (optional) - default value if the given iterable is empty  g = max([],default=9) here my iterable is empty and default set to 9 so 
# function will return 9
# key (optional) - key function where the iterables are passed and comparison is performed based on its return value ( key = value )
print("                                      max()")
a = [1,2,3,4,5]
print(max(a))

print(max(0.0001,0.01,1,2,3,4,5,6,7,8,999,999999))

a = ["Bilal","Hamza","Abuzar"]
print(max(a))

# now if we want min function to work like that if i pass an iterable in min function so min function return the longest string in iterable
# for this purppose i need to make a function that takes item and return its length
def len_item1(item):
    return len(item)

a = ["Bill","Abuzar","Harison","Barry"] 
print(max(a, key = len_item1))  # now here i can use that function len_item in key 


students = [ {"name":"Bilal" , "score":80 , "age":20 },
             {"name":"Hamza" , "score":75 , "age":25 },   
             {"name":"Zeeshan" , "score":90 , "age":21}
           ]
print(max(students, key = lambda item : item.get("score"))["name"])
# print(max(students[, key = lambda item : item.get("score"))["name"]])
print(max(students, key = lambda item : item.get("score"))["name"])