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
# loop = list(map(int,input().split())) # this is to take input from user and convert all its given numbers in integers and make a list of 'em
# print(loop)
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
a = [1,2,3,4,5,6]
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
# whenever iter() and next() applied on an object(list,tuple,etc), this object is called iterable 
# or anything on which we can apply for loop is called iterable
# ______________________________________________________________________________________________________________________________________________
# The next() function returns the next item in an iterator.
# You can add a default return value, to return if the iterable has reached to its end.
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
# line no 123 is also a iterator and i can iterate over it by next func.
# ______________________________________________________________________________________________________________________________________________
print("                                     zip()")
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
# syntax - zip(iterator1, iterator2, iterator3 ...)
# iterator1, iterator2, iterator3 ...	Iterator objects that will be joined together
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
for k in zip(l1,l2):
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