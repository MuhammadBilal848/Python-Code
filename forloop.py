# if we want to do a task multiple times we use loop for this purpose which is an efficient way.
# in python we have two types of loops "For Loop" & "While Loop"
# What if we want to write our name 10 times by using loops.
for a in range(10): # it starts from 0,1,2,..,10 here 10 will not included
    print("BILAL")    
# the first time this loop runs the value from range comes to variable "a" starts from 0 and loop will executed, the 
# second time another value from range comes to variable which is 1 and loop will again executed and so on so on.
for a in range(10): 
    print(a,"BILAL")
# we can also give starting point to range.
for b in range(1,10):
    print(b)
for b in range(2,9):
    print(b)
for b in range(3,8):
    print(b)
# we can also give step argument in range funtion.
for b in range(1,10,2): # 12345678910
    print(b)
for b in range(1,10,4):
    print(b)
List=["Bilal","Saboor","Araib","Saad","Uzair","Hamza","Ali"]
for a in range(6):
    print(List[a])
for a in range(0,6):
    print(List)
for num in [11,22,33,44,55,66,77,88,99]:
    print(num)
country= "Pakistan"
for char in country:
    print(char) # when we put a variable(contains string) on range's place interpretor starts print characters.
country= "Pakistan","Turkey" # this is tuple where applying parenthesis is optional.
for char in country:
    print(char)
for number in range(10):
    if number%3==1:
        break          # in break loop will be terminated
    print(number)
for number in range(10):
    if number%3!=0:        # here "!="" is not equal to
        break
    print(number)
for number in [5,7,11,22,90]:
    if number%3==0:
        break
    print(number)   
for number in range(10):        
    if number==7 or number==3 or number==9:
        continue 
    print(number)    
for number in range(10):        
    if number==7 and number==3 and number==9:
        continue 
    print(number)


