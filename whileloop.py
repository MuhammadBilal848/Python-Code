# we  use while loop to iterate a process many times.
# while loop works untill the condition is false.
# they were similar to for loop but differ in the sense that it allows user to terminate loop  by setting flags
i = 1
while i<=10:
    print(i,"Muhammad Bilal Haneef Qureshi")
    i=i+1
i = 1
j = int(input("How many times you want to check the remainder: "))
while i<=j:
    a = i%3
    print(f"Remainder of {i} is {a}")
    i = i + 1 
#  ---------**************-----------------
i = 1
j = int(input("How many times you want to check the remainder: "))
while i<=j:
    if i%3==0:
        break    
    print(i)
    i = i + 1 
# -------------************---------------
i = 1
j = int(input("Type number here: "))
while i<j:         
    i = i + 1 
    if i==1 or i==3 or i==5:
        continue    
    print(i)
flag = True
list = []
while flag:
    a = input("Enter your favourite food name: ")
    if a=="Quite":
        flag=False
    else:
        list.append(a)
print(list)