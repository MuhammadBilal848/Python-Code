# set comprehension - with the help of this we can create set in single line
s = { a**2 for a in range(1,11) }
print(s)

l = ["Bilal","Abuzar","Usama","Nofil","Zaigham"]
name = { n[0] for n in l }
print(name)