# in dictionaries of list we create a list in which all members are list
name_ls =  ["Bilal","Araib","Uzair","Saad","Saboor","Farhan"]
age_ls =   [  18   ,   17  ,   17  ,  19  ,   24   ,    19  ]
class_ls = [  12   ,   12  ,   12  ,  12  ,   12   ,    12  ]
stud_info = { "name":name_ls , "age":age_ls , "class":class_ls }
print(stud_info)
print(stud_info["name"][2]) 
print(stud_info["age"][2]) 
print(stud_info["name"][4]) 
print(stud_info["age"][4]) 