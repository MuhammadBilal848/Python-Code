# The capitalize() method returns a string where the first character is upper case. This method has no parameters
print("capitalize()")
a = "hi whatsup"
print(a.capitalize())
###########################################################################
# The casefold() method returns a string where all the characters are lower case. This method has no parameters
print("casefold()")
a = "HELLO, AND WELLCOME TO MY WORDL!"
print(a.casefold())
# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that 
# it will convert more characters into lower case, and will find more matches when comparing two strings and both are
# converted using the casefold() method
###########################################################################
print("center()")
a = "Bilal"
# if we want to add something(such as special characters etc ) before and after our string we use "center method".
# This method has two parameters first one named as "witdth" so in this parameter we pass how many special charater etc.
# we want to add bef/aft our string by adding it to length of the string and the second parameter named ""fillchar"
# so whatever we want to add bef/aft our string we that in this parameter inform or string
a = a.center(9,"#") 
# so in this case my string length is 5 and i want to add two hashes(#) bef/aft my code so len of str is 5 and i want
# to add total of 4 hashes (5 + 4 = 9)
print(a)
b = "Bilal"
b = b.center(13,"&")
# so in this case my string length is 5 and i want to add four ands(&) bef/aft my code so len of str is 5 and i want
# to add total of 8 ands (5 + 8 = 9)
print(b) 
c = "Bilal"
c = c.center(6,"@")
# so in this case my string length is 5 and i want to add 1 at(@) bef my code so len of str is 5 and i want
# to add total of 1 at (5 + 1 = 6)
# if  we want to add something to only one side then center method will add this to right side 
print(c) 
###########################################################################








###########################################################################
# The count() method returns the number of times a specified value appears in the string.
# This has three parameters(value,start,end) , in value parameter we pass a particular character that we want to 
# check that how many times it appear in my string and in second parameter we pass index number from where i want my
#  interpreter to check that character and in the third parameter we pass index number to where i want interpretor to
# check that character  
print("count())")
txt = "I love apples, apple are my favorite fruit"
txt = txt.count("a")
print(txt)
txt1 = "I love apples, apple are my favorite fruit"
txt1 = txt1.count("a",0,20)
print(txt1)
###########################################################################
# # if we want to check the string is end with particular text we use "endswith" method
# The endswith() method returns boolean , True if the string ends with the specified value, otherwise False.
# This has 3 parameters (value,start,end) , in value parameter we pass a particular character/string etc that we want
# to check that if is present in the end of my string  or not and in second parameter we pass index number from where
# i want my interpreter to check that character and in the third parameter we pass index number to where i want 
# interpretor to check that character
print("endswith()")
c = "Hello my name is Bilal"
print(c.endswith("Bilal"))
print(c.endswith("Bilal",0,16))
###########################################################################
# if we use \t in our string to add onetab space and we want to use tab but not that much spaces that /t gives us
# so we use "expandtabs" method. 
# This has 1 parameter named space-tabs in which we pass number of spaces wa want
print("expandtabs()")
a = "Pakistan\tis\ta\tpeace\tloving\tcountry"
print(a.expandtabs(5))
###########################################################################
# The find() method finds the first occurrence of the specified value.
# This has 3 parameters(value,start,end) , in value parameter we pass a particular character etc that we want
# to check that at what position that char. is present in my string and in second parameter we pass index number from where
# i want my interpreter to check that character and in the third parameter we pass index number to where i want 
# interpretor to check that character
# This method is same as index method but the differece is that the index() method raises an exception if the value
# is not found and find method return -1 if value is not present.
print("find()")
a = "I love apples, apple are my favorite fruit"
a = a.find("f")
print(a)
b = "I love apples, apple are my favorite fruit"
b = b.find("H")
print(b)
#############################################################################
# The format() method formats the specified value(s)  and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the 
# Placeholder section below.
print("format()")
print("Hello {} nice to meet you",format("Bilal")) 
print("Hello {name1} nice to meet your brother {name2}".format(name1 = "Bilal", name2 = "Hamza"))
print("hello {} how are you {} nice to meet you {}".format("BILAL","Hamza","Abuzar"))
a = "bilal"    # if we want to use different variables in different place holder we pass index of that variable in 
c = "haneef"   # that place holder and indexing starts from 0---------> n
b = "qureshi"
print("Your first name is {0} second is {2} third is {1}".format(a,b,c))
#############################################################################
# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() method is almost the same as the find() method, the only difference is that the find() method 
# returns -1 if the value is not found.
print("index()")
a = "Hello everyone my name is bilal"
print(a.index("H"))
# print(a.index("H",1,-1))
# This has 3 parameters(value,start,end) , in value parameter we pass a particular character etc that we want
# to check that at what position that char. is present in my string and in second parameter we pass index number from where
# i want my interpreter to check that character and in the third parameter we pass index number to where i want 
# interpretor to check that character
#############################################################################
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) 
# and numbers (0-9).
# Example of characters that are not alphanumeric: (space)!#%&? etc.( if spaces are added b/w string that divides 
# num and aphabet, the string is no more aplha-numeric and if string has only one character this will also counted
# as alpha-numeric)
print("isalnum()")
a = "Pakistan1232"
print(a.isalnum())
a = "Pakistan 1232"
print(a.isalnum())
a = "Alphanumeric_123"
print(a.isalnum())
#############################################################################
# The isalpha() method returns True if all the characters are alphabet letters (a-z).
# Example of characters that are not alphabet letters: (space)!#%&? etc.("Hello" # string, if spaces are added is a  
# string that divides the words b/w a string, the string is no more aplhabetical)
print("isalpha()")
a = "Bilal"
print(a.isalpha())
a = "Bilal Haneef"
print(a.isalpha())
a = "456"
print(a.isalpha())
#############################################################################
# isdecimal()-It is a function in Python that returns true if all characters in a string are decimal. If all characters
# are not decimal then it returns false.
# This has no parameter
#  True – all characters are decimal
# False – one or more then one character is not decimal.
print("isdecimal()")
a = "123456789"
print(a.isdecimal())
a = "12345Bilal6789"
print(a.isdecimal())
a = '\u00B2'
print(a.isdecimal()) # for unicode isdecimal returns false
#############################################################################
# In Python, isdigit() is a built-in method used for string handling.
# The isdigit() methods returns “True” if all characters in the string are digits, Otherwise, It returns “False”.
# This has no parameter
# 1.True- If all characters in the string are digits.
# 2.False- If the string contains 1 or more non-digits.
# isdigit and isdecimal are same but differ at unicode
print("isdigit()")
a = "123456789"
print(a.isdigit())
a = "12345Bilal6789"
print(a.isdigit())
a = '\u00B2'
print(a.isdigit())
#############################################################################
# The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# This has no parameter
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or 
# underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print("isidentifier()")
a = "Alphanumeric123" # this is alphanumeric string
print(a.isidentifier())
a = "Alphanumeric 123" # this is not alphanumeric string
print(a.isidentifier())
a = "Alphanumeric_123" # this is alphanumeric string
print(a.isidentifier())
#############################################################################
# The islower() method returns True if all the characters are in lower case, otherwise False.
# This has no parameter
# Numbers, symbols and spaces are not checked, only alphabet characters.
print("islower()")
a = "this is lower string"
print(a.islower())
a = "This is lower string"
print(a.islower())
a = "this is lower strinG"
print(a.islower())
#############################################################################
# The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
# Exponents, like ² and ¾ are also considered to be numeric values
print("isnumeric()")
a = "123"
print(a.isnumeric())
a = "123Hello123"
print(a.isnumeric())
a = '\u00B2' # unicode 
print(a.isnumeric())
#############################################################################
# The isprintable() method returns True if all the characters are printable, otherwise False.
# This function is used to check if the argument contains any printable characters such as :
# Digits ( 0123456789 )
# Uppercase letters ( ABCDEFGHIJKLMNOPQRSTUVWXYZ )
# Lowercase letters ( abcdefghijklmnopqrstuvwxyz )
# Punctuation characters ( !”#$%&'()*+, -./:;?@[\]^_`{ | }~ )
# Space ( )
# This has no parameter 
# 1.True- If all characters in the string are printable or the string is empty.
# 2.False- If the string contains 1 or more non printable characters.
print("isprintable()")
a = "Hello!\nAre you #1?"
print(a.isprintable())
a = "0123345"
print(a.isprintable())
a = "hello @#$#$%%%%%^$%&%^* "
print(a.isprintable())  
#############################################################################
# The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
# this has no parameter
print("isspace()")
a = "    "
print(a.isspace())
a = "   B   "
print(a.isspace())
#############################################################################
# The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word
# are lower case letters, otherwise False.
# This has no parameter
#  Symbols and numbers are ignored.
print("istitle()")
a = "hello world!"
print(a.istitle())
a = "Hello World!"
print(a.istitle())
a = "hello World!"
print(a.istitle())
a = "Hello World 123"
print(a.istitle())
a = "Hello world 123"
print(a.istitle())
#############################################################################
# The isupper() method returns True if all the characters are in upper case, otherwise False.
# this has no parameter
# Numbers, symbols and spaces are not checked, only alphabet characters.
print("isupper()")
a = "Hello Welcome To My World!"
print(a.isupper())
a = "HELLO WELCOME TO MY WORLD!"
print(a.isupper())
a = "HELLO WELCoME TO MY WoRLD!"
print(a.isupper())
a = "HELLO_WORLD 123"
print(a.isupper())
a = "HELLO WORLD 123"
print(a.isupper())
#############################################################################
# The join() method is a string method and returns a string in which the elements of sequence 
# have been joined by str separator.
# Parameters: The join() method takes iterable – objects capable of returning its members one 
# at a time. Some examples are List, Tuple, String, Dictionary and Set
print("join()")
a = "Hello World!"
sep = "#"
print(sep.join(a))
a = "Hello World!"
print("@@@".join(a))
print("-_-".join(a))
#############################################################################
# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
# Parameters :
# len : The width of string to expand it.
# fillchr (optional): The character to fill in remaining space.
# Return Value :
# The resultant left aligned string expanding the given width.
print("ljust()")
a = "Hello in user how are you"
print(a.ljust(26,"%"))







