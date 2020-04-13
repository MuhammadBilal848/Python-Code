# dictionary comprehension - with the help of this we can create dictionary in single line
# syntax - {key: value for vars in iterable}
dictionary = {  }
for a in range(1,11):
    dictionary[a] = a*a
print(dictionary)
# now we do this by using dictionary comprehension
dicto = { num : num*num for num in range(1,11) }
print(dicto)
# now we modify this to something like this {"square of 1": 1 ,"square of 2":4 }
e_tron = { f"Sqaure of {num}" : num*num for num in range(1,11) }
print(e_tron)
for a in e_tron.items():
    print(a)
# ________________________________________________________________________________
l = ["Bilal","Abuzar","Usama","Nofil"]
dol = { name : len(name) for name in l }
print(dol)
# ________________________________________________________________________________
n = "Bilal Haneef"
d = { char : n.count(char) for char in n }
print(d)
################################### DICTIONARY COMPREHENSION WITH IF-ELSE ##################################
# syntax - {key: (<expression> if (condition) else <expression>) for vars in iterable}
s = { a : "even" if a%2==0 else "odd" for a in range(1,11)}
print(s)
# ________________________________________________________________________________
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)