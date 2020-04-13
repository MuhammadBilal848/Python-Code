# CSV(comma separated values) files are the text-only files that are simplified version of a spreadsheet or data base
# what if we want to read an existing cvs file    
import csv
# if we didnt give "open" any parameter it by default read the file
with open("first.csv","r") as file:
    a = csv.reader(file)
    for content in a:
        print(content)
# Thats how we read data in csv files
# now we how do we write a non-existing file we use writer mode for this
# this mode will create file itself if its not exist in system 
with open("first222.csv","w") as file1:
    b = csv.writer(file1)
    b.writerow([1996,"Hockey","Pakistan"])
with open("first222.csv","r") as file:
    g = csv.reader(file)
    for content in g:
        print(content)
# now we want to write file without overwriting
# we use append mode for this
with open("first222.csv","a",newline="") as file1:
    b = csv.writer(file1)
    b.writerow([1998,"GDG","Pakistan"])
with open("first222.csv","r") as file:
    g = csv.reader(file)
    for content in g:
        print(content)