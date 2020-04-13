print(123) # to print any numerical value we dont need to use double/single quotes 
# the data which we have given to print func.  above is called "Integer Data or Integer  Value"
print(123,456) # print function can print more than one value at a time              
print(1233, 67778 ,7677)
print() # if write nothing in print funtion it still working but due to being empty it shows nothing.
print(80.18)
# the data which we have given to print func.  above is called "Floating Data or Floating Point Value"
#                ---------------********************************-------------------
print("Hello World") # anything that will be written in double/single quotes is called "String Data or String Value"
# the data which we have given to print func.  above is called "String Value"
print("21") #this is also called "String value"
print("Pakistan123") #this data is called "Alphanumeric Data"
print("Bilal",'Haneef',"Qureshi") #comma is signal that new value has been started
# in the above print function we have'nt told the funtion to give space b/w the string value, so where it comes from
# actually print function is a predefined function and in its signature(seen by placing a cursor on print) comma 
# is used as a separator(sep=" ")
print("Bilal",'Haneef',"Qureshi",sep="") # where sep is a separator, anything that will be written b/w its quotes -
# used as separator between tha value.
print("Bilal",'Haneef',"Qureshi",sep="  ")
print("Bilal",'Haneef',"Qureshi",sep="#**#")
#                ---------------********************************-------------------
print("Hello World 1")
print("Hello World 2")
print("Hello World 3")
# in the above lines(22,23,24) we have written a simple code but we have'nt told the function to print 22 line
#in the next line and the line 23 in the other next line. So why did it happens. It happend due to the escape 
#character(end="/n") which is predefined in signature of print function. "\n" means new line has been started 
print("Hello World 1",end='')
print("Hello World 2",end='')
print("Hello World 3")
print("Hello World 1",end='_**_')
print("Hello World 2",end='_**_')
print("Hello World 3")
print("Hello World 1", end='\t')
print("Hello World 2", end='\t')
print("Hello World 3")
print("Hello World 1", end='\t\t')
print("Hello World 2", end='\t\t')
print("Hello World 3")
print("Hello World 1", end='\n')
print("Hello World 2", end='\n')
print("Hello World 3")
print("Hello World 1", end='\n\n')
print("Hello World 2", end='\n\n')
print("Hello World 3")
print("Hello World 1", "first",sep=':)',end='_**_')
print("Hello World 2", "second",sep=':)',end='_**_')
print("Hello World 3", "third",sep=':)')
print("Bilal Haneef Qureshi")
#            -----------------------****************---------------------------
#                                   Escape Sequences                      
print("Bilal\\Haneef\\Qureshi") # \\=\
print("Bilal\\\\Haneef\\\\Qureshi") #\\\\=\\
print("Bilal\'Haneef\'Qureshi") # \' = '
print("Bilal\"Haneef\"Qureshi") # \" = "
print("Bilal\bHaneef\bQureshi\b") # ab\b =a (\b is called ascii backspace)
print("Bilal\fHaneef\fQureshi") # \f is called ascii formfeed