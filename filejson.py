# first we have to import json 
# writing data to json files, for writing file in json we use "dump" method
import json
with open("firstfile1.json","w") as f:
    json.dump(["bilal","zeeshan","hamza","Haneef"],f)
# # if we didnt give any mode in parameter of open it by default read the file
# with open("firstfile.json","r") as d:
#     a = json.load(d)
#     print(a)
# # if we again write the same file write mode will overwite the file
# # thats why we use append mode 
# with open("firstfile.json","a") as d:
#     json.dump([19,39,26],d)
# with open("firstfile.json","a") as d:
#     json.dump([12,13,14,12455],d)
