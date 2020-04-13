# in list of dictionaries we create a list in which all members are dictionaries
students = []
students.append( { "name":"bilal" , "class":"12" , "sec":"C" , "center":"saec" , "age":18} )
students.append( { "name":"Araib" , "class":"12" , "sec":"B" , "center":"saec" , "age":17} )
students.append( { "name":"Aashir" , "class":"12" , "sec":"A" , "center":"saec" , "age":17} )
print(students)
print(students[0]["sec"])
print(students[1]["sec"])
print(students[2]["sec"])
print(students[2]["age"])
# ------------*************---------------
for a in students[0].keys():
    print(a)
for a in students[0].values():
    print(a)
for a,b in students[0].items():
    print(a,b)
# ------------*************---------------
for a in students[1].keys():
    print(a)
for a in students[1].values():
    print(a)
for a,b in students[1].items():
    print(a,b)
