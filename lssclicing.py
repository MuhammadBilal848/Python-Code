# what if we want to access multiple elements from the list, we use slicing method.
#-veindex -8        -7        -6       -5           -4             -3          -2        -1
list1=["Karachi","Lahore","Islamabad","KPK","Gilgitbaltistan","Hyderabad","Moenjodaro","Sindh"]
#=veindex  0         1         2        3            4             5            6          7
print(list1[3])
print(list1[-5])
# we want to access 4 elements in b/w the list. we can access multiple list elements by writing list name and in square
# brackets we type semicolon(inclusive:exclusive) before colon we write the value from we want to get elements
# and after colon write the value from we want to end our list but exclusive works in 1 less value(n-1)  
print(list1[2:6]) # here exclusive(6-1=5)
print(list1[-6:-2])
print(list1[:]) # it prints whole list
print(list1[2:])
print(list1[:7]) # it starts from 0
print(list1[3:-1])
print(list1[2:-8]) # here it starts from 2 but inclusive always works in forward direction and -8 index is not in
# forward direction.
# now we use step argument.
# step argument means when first character will print how much step should interpreter will take in character seq.
# syntax [ start argument : stop argument : step argument ]
# step argument cannot be zero
print(list1[0:8:2])
print(list1[-8:8:4])
print(list1[::7])
# if we want to reverse the list we just need to give step argument -1 value.
print(list1[::-1])