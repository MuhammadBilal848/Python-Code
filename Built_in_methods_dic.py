# format_map() function is an inbuilt function in Python, which is used to return an dictionary key’s value.
# this has only one parameter in which we pass the dictionary's name
a = { "StudentName":"Bilal" , "FatherName":"Haneef"}
print("{StudentName} second name is {FatherName}".format_map(a))
#############################################################################
# The join() method is a string method and returns a string in which the elements of sequence 
# have been joined by str separator.
# Parameters: The join() method takes iterable – objects capable of returning its members one 
# at a time. Some examples are List, Tuple, String, Dictionary and Set
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict.keys())
print(x)
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict.values())
print(x)
#############################################################################
# what if we want to copy the complete dic.
# in order to copy the dic. we use copy  function.
a = {'name': 'Bilal', 'age': 19, 'gender': 'male', 'religion': 'islam'}
# copy function works "By Value" 
# # in this method the new DIC will form completely separate from the copied one, and if we ADD            
#  any KEY to that DIC from which we made a copy, we will not see any change in the copied one. 
print(a)
print("                                     copy()")
b = a.copy() # by value
print(b)
b["Mobile"] = "Xiaomi"
print(b)
print(a)
# # another way to copy dic, is by assigning the dic to other variable.                                   
# there is a difference b/w copy dic via copy funtion and assigning dic to varaible.
first = {'name': 'Bilal', 'age': 19, 'gender': 'male', 'religion': 'islam'}
print(first)
second = first
print(second)
# this is called copy by reference 
# in this method the members of dic do not copy in the variable but the reference of dic copies in it.
#  in this method if we do any sort of change in second we will see that change in first. 
second["mobile"] = "Xiaomi"
print(second)
print(first) 
#############################################################################
# The fromkeys() method returns a dictionary with the specified keys and the specified value. 
# agar hum chahaty hain ke different keys ki same values hon to uske kiye formkeys use karty hain
# this has two parameters(iterable,values=None)
print("                                     fromkeys()")
x = ("key1","key2","key3")
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)
# another example
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)
#############################################################################
# The get() method returns the value of the item with the specified key.
# this has two parameters(keyname,value=default(none) or A value to return if the specified key do not exist.)
print("                                     get()")
a = {
    'name': 'Bilal',
    'age': 19,
    'gender': 'male', 
    'religion': 'islam', 
    'mobile': 'Xiaomi'
    }
print(a.get("mobile"))
print(a.get("email"))
print(a.get("email",500)) # if we not want get method to return none we can use value intead comma separated
#############################################################################
# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
print("                                     keys()")
a = {'name': 'Bilal','age': 19,'gender': 'male', 'religion': 'islam', 'mobile': 'Xiaomi'}
b = a.keys()
# The view object will reflect any changes done to the dictionary, see example below.
a["number"] = 56
print(b)
#############################################################################
print("                                     values()")
# The values() method returns a view object. The view object contains the values of the dictionary, as a list.
a = {'name': 'Bilal','age': 19,'gender': 'male', 'religion': 'islam', 'mobile': 'Xiaomi'}
b = a.values()
# The view object will reflect any changes done to the dictionary, see example below.
a["number"] = 56
print(b)
#############################################################################
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, 
# as tuples in a list.
print("                                     items()")
a = {'name': 'Bilal','age': 19,'gender': 'male', 'religion': 'islam', 'mobile': 'Xiaomi'}
b = a.items()
# The view object will reflect any changes done to the dictionary, see example below.
a["number"] = 56
print(b)
#############################################################################
# The pop() method removes the specified item from the dictionary.
# The value of the removed item is the return value of the pop() method, see example below.
# this has two parameters(keyname,value=default(none) or A value to return if the specified key do not exist.)
print("                                     pop()")
a = {'name': 'Bilal', 'age': 19, 'gender': 'male', 'religion': 'islam'}
b = a.pop("age")
print(a)
print(b)
#############################################################################
# The popitem() method removes the item that was last inserted into the dictionary.
# In versions before 3.7, the popitem() method removes a random item.
# The removed item is the return value of the popitem() method, as a tuple, see example below.
print("                                     popitem()")
a = {'name': 'Bilal', 'age': 19, 'gender': 'male', 'religion': 'islam'}
b = a.popitem()
print(b)
#############################################################################
# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value, see example below
# this has two parameters(keyname,value=default(none) or A value to return if the specified key do not exist.)
                                            #   or
# If the key exist, this parameter has no effect, If the key does not exist, this value becomes the key's value, Default value None
print("                                     setdefault()")
a = {
    'name': 'Bilal',
    'age': 19,
    'gender': 'male', 
    'religion': 'islam', 
    }
b = a.setdefault("religion","no value")
print(b)
# If the key exist, this parameter has no effect, If the key does not exist, this value becomes the key's value, Default value None
# example 
a = {
    'name': 'Bilal',
    'age': 19,
    'gender': 'male', 
    'religion': 'islam', 
    }
b = a.setdefault("mobile","xiaomi")
print(b)
#############################################################################
# The update() method inserts the specified items to the dictionary.
# The specified items can be a dictionary, or an iterable object.
print("                                     update()")
a = {
    'name': 'Bilal',
    'age': 19,
    'gender': 'male', 
    'religion': 'islam', 
    }
a.update({"Mobile":"samsung"})
print(a)



