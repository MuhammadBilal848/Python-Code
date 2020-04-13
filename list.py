# what if we want to store hundreds or thousands of values then we have to make hundreds or thousands of variable
# which for us is quite hard to remember thats why list comes into play. By using list we can store hundreds or thousands of
# values in a single variable and we only have to remember is the list name for access it. 
# what if we wanted to store multiple values in a single variable which termed as "Bunch of values in a single varaible"
# the variable in which we want to store multiple values is called "List type variable".(other languages have arrys)
# in list every value has its particular index(position) by default the first value has "0" index value second value
# has "1" third value has "2" and so on so on.
# list contain multiple data types in it. In a list we can use string,integer or float data and so on so on.
first_list=["Bilal","Saboor","Araib","Saad","Uzair"]
# index        0       1        2      3       4
# thats how we make list(line 9)
# in the next step we access the list members.
print(first_list[0])
print(first_list[1])
print(first_list[2])
print(first_list[3])
print(first_list[4])
###############################################################
a = [1,2,3]
print(a*3) # this will make same element in list 3 times
###############################################################
l = ["one",'two',"three",'four',"five"]
l[1:] = 2,3,4,5 # if i want to change all the elements of my list from a particular stop argument i do this.
print(l)
##############################################################
lf = ["one","two"]
ls = ["three","four"] # in this way we add two or multiple lists together and if we want to x,/,+,- list of integers we need  to use numpy and 
# pandas which are data science libraries   
print(lf+ls)
##################################################################
l_one = ["one",'two',"three",'four',"five"]
l_two = ["one",'two',"three",'four',"five"]
l_three = ["one",'two',"three",'four',"five","six","seven","eight","nine","ten"]
print(l_one == l_two) # ==(equal to operator) compares element of list that whether they are same or not 
print(l_one is l_two) # is opeartor check wheter both list placed at same memory or not(so here both object l_one and l__two
# are different so it will return false)
##################################################################
# convert string into list 
# split method
name_age = "Bilal 20"
print(name_age.split())
name_age = "Bilal$20"
print(name_age.split("$"))
name_age = "Bilal,20"
print(name_age.split(","))
name_age = "Bilal#20"
print(name_age.split("#"))
# convert list into string
# join method
# The join() method is a string method and returns a string in which the elements of sequence 
# have been joined by str separator.
# Parameters: The join() method takes iterable – objects capable of returning its members one 
# at a time. Some examples are List, Tuple, String, Dictionary and Set
l = ['Bilal', '20']
# synax to join list to string
# "character we want to join with".join(listname)
print(" ".join(l))
##################################################################
# in order to check length of our list we use len function.
print(len(first_list)) # we have 5 elements in our list.
# now we want to add element in our list in the end/tail of the list.
first_list.append("Farhan") # we can append only one value through append function.
print(first_list[5])
print(first_list)
# what append funtion did is add the element in the list in the end/tail. Anything which will written b/w append's 
# brackets will be added to list.
print(len(first_list))
# what if we want to add an element at any index(0,1,2,3,.....).
# for this we use insert function.
first_list.insert(2,"Ali")
print(first_list)
# what insert function did is add that  element in the list at our desireable index. Anything which will written b/w
# insert's brackets separated with comma (before comma we write index value and after comma we write our elements)
# what if we want to append multiple values in list.
# in order to append multiple values we use extend function. Anything which will written b/w circular brackets inside
# square brackets will append to the list.
first_list.extend(["Aashir", "Wasay"])
print(first_list)
print(len(first_list))
print(first_list.count("Bilal")) # count function checks how many times does the word written b/w brackets used.
# what if we want to know on which index an element is placed.
print(first_list.index("Ali"))
# print(first_list.index(0))
# what if we want to copy the complete list.
# in order to copy the list  we use copy  function.
second_list=first_list.copy() # copy function works "By Value"                                                  
# in this method the new list will form completely separate from the copied one, and if we append             
#  any element to that list from which we made copy, we will not see any change in the copied one.              
first_list.append("Zeeshan")                                                                               
print(first_list)                                                                                              
print(len(first_list))                                                                                         
print(second_list)                                                                                                           
print(len(second_list))                                                                                                                                                                                                              
# another way to copy list, is by assigning the list to other variable.                                   
# there is a difference b/w copy list via copy funtion and assigning list to varaible.                       
third_list=second_list # this method of copying the list works "By reference"                            
# in this method the members of list do not copy in the variable but the reference of list copies in it.
#  in this method if we do any sort of change in second_list we will see that change in third_list.             
print(third_list)                                                                                                
# what if we want to clear all the element from list.
# we use clear function to clear list
first_list.clear()
print(len(first_list))
# what if we want to delete a particular item from the list.There are two methods first is Del and second is remove
del second_list[6] # in the squre bracket we write the index number which we want to delete from the list
# del isn't a function it is a statement
print(second_list) # del statement permanentely delete element from the list and the value cannot be recover. 
# now we use remove funtion to remove element from the list.
second_list.remove("Wasay")
print(second_list)
second_list.remove("Aashir")
print(second_list)
# what if we want to remove a value such that it can remove from list but stored somewhere.
# for this purpose we use pop function. what pop do is store that value in another variable after removal of value.
popped=third_list.pop()
print(f"The popped item is {popped}")
print(f"The remaining items are {third_list}")
# we can pop any element by just writing its index number in circular brackets of pop function
popped1=third_list.pop(2)
print(popped1)
print(first_list)
# what if we want to do correction in our list is such a way that the element of list written in aplhabatic order.
# for this purpose we use sort method or function
# by default sort function sort elements in accending order(a,b,c,d,e,f,g,..............)
print(third_list)
third_list.sort()
print(third_list) # this sorting is accending reverse function is false in sort function
# if we want to sort element with decending order(z,y,x,w,v,u) what we do is just true reverse funtion in sort function.
third_list.sort(reverse=True)
print(third_list)
# if we want to sort our element in such a way to save our variable after sorting so we use sorted function
a = [4,2,3,5,6,7,8,9]
b = sorted(a) 
print(b)
###################################
a = [4,2,3,5,6,7,8,9]
b = sorted(a, reverse=True) 
print(b)
############################################
a = [2,3,4,5,66,776,87,5,1,54,]
a.sort()
print(a)
b = ['Abuzar', 'Usama', 'Hasan', 'hasham', 'nofil', 'uzair', 'araib', 'ashir']
b.sort()
print(b)
#########################################################################################
lf = ["one","two"]
ls = ["three","four"]
print(lf+ls)
#########################################################################################
l_one = ["one",'two',"three",'four',"five"]
l_two = ["one",'two',"three",'four',"five"]
l_three = ["one",'two',"three",'four',"five","six","seven","eight","nine","ten"]
print(l_one == l_two) # ==(equal to operator) compares element of list that whether they are same or not 
print(l_one is l_two) # is opeartor check wheter both list placed at same memory or not(so here both object l_one and l__two
# are different so it will return false)
#########################################################################################
#                                                       list vs python
# in C , C++ and Java
# In the aboe lang. arry is used and we can only store same data types in an arry(means all string elements,all integer elements etc)
# we dont use arry module much in python because it does not have flexibility in it instead we use numpy arrys(numpy is a data science library)
# nunmpy arrys - binding with c libraries
# list - store any data = flexible
# But in python we can store multiple data types in single list

# python arry module = fix data type
# python have arry moodule by which we can use arry(fix data type) which have same characteristics as other programming languages have.

# javascript arry = python list (both are flexible)