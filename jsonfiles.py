# to use "json" methods we have to import "json" module
import json
# json stands for Javascript object 
# json file has .json extention.
# usually data structures like dictionary stored in  json files.

# __________________________________ Reading JSON File ______________________________________________

# to read json file we have function called "load"
# json.load can deserialize a file itself i.e. it accepts a file object,
# syntax - json.load(alias)
# with open("j_one.json","r") as j1:
#     print(json.load(j1))

# ____________________________________________ Writing CSV File _________________________________________

# to write into csv file we have function called "dump"
# syntax - json.dump("file-name",alias)
# with open("j_one.json","w") as j2:
#     json.dump("over-write text",j2)


# d = {"Bilal":20,"Abuzar":19,"Usama":190,"Zaigham":200}
# with open("j_one.json","a") as j3:
# json.dump(d,j3)

# _________________________________________________________________________________________

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# if i have dictionary in form of string in my json file, to access its key,values i can parse it using loads
# json.loads() deserialize string.
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# # parse x:
# y = json.loads(x)
# # the result is a Python dictionary:
# print(y["age"])

# # _________________________________________________________________________________________

# # Convert from Python to JSON
# # If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# # convert into JSON:
# y = json.dumps(x)
# # the result is a JSON string:
# print(y)
# print(type(y))

# you will more information about load and loads , here 
# https://stackoverflow.com/questions/39719689/what-is-the-difference-between-json-load-and-json-loads-functions

# with open("j_one.json","r") as f:
#     print(json.load(f))
    
# with open("j_one.json","r") as f2:
#     print(json.loads(f2)) # this will cause error because loads will deserialize only string not file object

# with open("j_one.json","r") as f3:
#     print(json.loads(f3.read())) # here f2.read() will convert my file object data to str form which is laods
# requirement

 
with open("j_two.json","r") as f4:
    with open("j_one.json","a") as f5:
        json.dump(f4.read(),f5)