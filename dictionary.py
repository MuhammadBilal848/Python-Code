# syntax of dictionary
# Dictionary = { key:value , key:value , key:value }
my_dictionary = { "name":"Bilal" , "age":19 , "gender":"male" , "religion":"islam" }
print(len(my_dictionary))
print(my_dictionary)
# how to add new element in dictionary
# syntax for adding new value in dic.
# Dictionary[key]=value
my_dictionary["email"] = "bilalhanif848@gmail.com"
my_dictionary["mobile"] = 15
my_dictionary[80] = "first"
print(my_dictionary)
# how to access elements from dictionary
# syntax to access value from dictionary
# Dictionary[key]
print(my_dictionary["email"])
print(my_dictionary[80])
print(my_dictionary["name"])
# how to delete a key from dictionary
# syntax for deleting the key from dictionary
# del Dictionary[key]
del my_dictionary["mobile"]
print(my_dictionary)
# how to update/change a key value
my_dictionary["age"] = 18
print(my_dictionary) # same key can never be in a dictionary
# if we give dictionary a same key with multiple different values the previous ones are overwrite by the new ones
newDic = {1:100 , 2:200 , 3:300 , 4:400 , 5:500 , 1:10000000} # here we use key 1 two times with different values
print(newDic) # last one is overwrites first one because they have same key
# how to check whether a key presents in dictionary or not
# syntax for checking a key presents in dictionary or not
# key in Dictionary
print(80 in my_dictionary)
print(4 in newDic)
print(10 in newDic)
# how can we iterate items in dictionary
# there are three functions in dic. 
# i) key(provides only key) 
# ii) value(provides only value)
# iii) item(provides both key as well as value)
# ---------KEY------------
for a in my_dictionary.keys():
    print(a)
# --------VALUE----------
for a in my_dictionary.values():
    print(a)
# ------------ITEM----------
for a,b in my_dictionary.items():
    print(a,b)
    