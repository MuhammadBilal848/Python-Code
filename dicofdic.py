# in dictionaries of dictionaries we create a dictionary in which all members are dictionaries
name = { "Bilal":1 , "Araib":2 , "Uzair":3 , "Saad":4 , "Saboor":5 , "Farhan":6 }
young_age = { 1:18 , 2:17 , 3:17 , 4:18 , 5:24 , 6:18 }
children = { "wasay":1 , "javeria":2 , "vaniya":3 , "rabiyan":4 , "humaima":5 }
eld_age = { 1:18 , 2:17 , 3:17 , 4:18 , 5:24 , 6:18 }
dict = { "name":name , "young":young_age , "children":children , "elder":eld_age }
print(dict)
print(dict["children"]["vaniya"])
print(dict["young"][5])
print(dict["name"]["Farhan"])

