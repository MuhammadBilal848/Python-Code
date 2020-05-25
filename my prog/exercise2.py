# take two comma separated inputs from user
# 1. User name
# 2. a single character

#  output - print two lines
# 1. Uer name length
# 2. count the character that user inputed [ bonus: case insensitive count]
name , char = input("Put your name and anyone character comma separated: ").split(',')
total = name + char
print(len(name))
print( total.count(char) )
