# to use csv methods we have to import csv module
from csv import reader
# csv stands for "comma separated values" we use csv files to store tabular data(data in form of table) 
# csv file has .csv extention
# we can separate data through different delimiters(  ,  |  *  etc) but most commonly we use comma ,  if we change the delimeter we also have to 
# define that delimiter in reader / dictreader as keyword argument(we can define delimeiter in reader and dictreader mode)
# we can use two methods for reading csv file one is reader method other is dictreader
# to read file in csv we use reader function from csv module
# ______________________________________ Reading CSV File ______________________________________________
print("                             reader()")
with open("one.csv","r") as f:
    csv_data = reader(f) # this will return csv reader object
    for a in csv_data:
        print(a)

print("                             DictReader()")
from csv import DictReader
# to read csv file we have an other function called Dictreader which return ordered dictionary
with open("one.csv","r") as f1:
    csv_data1 = DictReader(f1) # this will return csv Dictreader object
    for a in csv_data1:
        print(a)
        print(a["name"])
    
# reading file using Dictreader is usefull, because it prints ordered dictionary

# now i have another csv file named two.csv in which values are pipe separated
with open("two.csv","r") as f3:
    d = DictReader(f3,delimiter ="|" )
    for a in d:
        # print(a)
        print(a["name"])

# ____________________________________________ Writing CSV File _________________________________________

# we can use two methods for reading csv file one is writer method other is dictwriter
from csv import writer 
print("                             writer()")
with open("file3.txt","w",newline='') as f4:
# now we have two methods of writing into csv file , writerow and writerows
    a = writer(f4)
# so here a is writer object in which i can write using writerow and writerows
    a.writerow(["name","gender","age"])
    a.writerow(["bilal","male","20"])
    a.writerow(["bilal","male","20"])
# this will write file with oneline space to remove space we can use newline keyword as open parameter

# now we write file using writerows
with open("file4.txt","w", newline='') as f5:
    b = writer(f5)
    b.writerows([["name","gender","age"],["bilal","male","20"],["hamza","male","25"]]) 
# by using writerows we dont need to write data in mulitple line we just have to write in a list 

# now we use dictwriter method to write into csv file
from csv import DictWriter
print("                             DictWriter()")
with open("file4.txt","w",newline='') as f6:
    dw = DictWriter(f6,fieldnames=["fname","lname","age"])
    dw.writeheader()  # this will write field name in the file
# note -  always pass header in fieldname as keyword argument in dictwriter
    dw.writerow({"fname":"bilal","lname":"haneef","age":20})
    dw.writerow({"fname":"hamza","lname":"haneef","age":25})
# note always passs data inform os dictionary in writerow and writerows
with open("file5.txt","w",newline='') as f7:
    dw = DictWriter(f7,fieldnames=["fname","lname","age"])
    dw.writeheader()  # this will write field name in the file
# note -  always pass header in fieldname as keyword argument in dictwriter
    dw.writerows([
    {"fname":"bilal","lname":"haneef","age":20},
    {"fname":"hamza","lname":"haneef","age":25},
    {"fname":"zeeshan","lname":"haneef","age":32}
    ])



# _____________________________________________________________________________________________________________________
# what if we want to read and write at the same time , for this we can do this

from csv import DictReader,DictWriter
with open("three.csv","r") as rf:
    with open("four.csv","w") as wf:
        c_read = DictReader(rf)
        c_write = DictWriter(wf,fieldnames=["F_name","Email","Age"])
        c_write.writeheader()
        for a in c_read:
            fname,eml,aGe = a["name"],a["email"],a["age"]
            c_write.writerow({"F_name":fname , "Email":eml,"Age":aGe})
