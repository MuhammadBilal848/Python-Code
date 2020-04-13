# list comprehension - with the help of t   his we can create list in single line
# syntax - [(expression)/(something we want to append) for item in list] --------> here square braces are included
a = []
for b in range(1,11):
    a.append(b**2)
print(a) 
# now we do this by using list comprehension
squares = [ a**2 for a in range(1,11)]
print(squares)
# code below works same but ugly syntax and took many lines
sq = []
[ sq.append(a**2) for a in range(1,11) ]
print(sq)
############################################################
ls = []
for a in range(1,11):
    ls.append(a*-1)
print(ls)
# now we do this by using list comprehension
lso = [ x*-1 for x in range(1,11)]
print(lso)
# code below works same but ugly syntax and took many lines
lson = []
[ lson.append(g*-1) for g in range(1,11) ]
print(lson)
############################################################
namel = ["Bilal","Hamza","Zeeshan"] # first method
emp = []
for a in range(len(namel)): # 0,1,2,3
    emp.append(namel[a][0])
print(emp)
namelo = ["Bilal","Hamza","Zeeshan"] # second method
empo = []
for a in namelo:
    empo.append(a[0])
print(empo)
# now we do this by using list comprehension
namelo = ["Bilal","Hamza","Zeeshan"]
nml = [ a[0] for a in namelo ]
print(nml)
n = []
namelo = ["Bilal","Hamza","Zeeshan"]
[ n.append(a[0]) for a in namelo ]
print(n)
###################################### LIST COMPREHENSION WITH IF ###############################
# syntax - [(expression)/(something we want to append) for item in list if (condition)] 
numbers = list(range(1,11))
nums = []
for a in numbers:
    if a%2==0:
        nums.append(a)
    else:
        continue
print(nums)
# now we do this by using list comprehension
even = [ a for a in range(1,11) if a%2==0 ]
print(even)
odd = [ a for a in range(1,11) if a%2!=0 ]
print(odd)
# _____________________________________________________________________________
###################################### LIST COMPREHENSION WITH IF-ELSE ###############################
# syntax - [ (expression) if (condition) else (expression) (expression)/(something we want to append) for item in list] 
num = list(range(1,11))
newl = []
for a in num:
    if a%2==0:
        newl.append(a*2)
    else:
        newl.append(-a)
print(newl)
# now we do this by using list comprehension
nums = [ a*2 if (a%2==0) else -a for a in range(1,11) ]
print(nums)
###################################### NESTED LIST COMPREHENSION ###############################
l = []
for a in range(3):
    l.append([1,2,3])
print(l)