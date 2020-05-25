# string sub sequences or string slicing
# if we want to print more than one character by its index number we always use string slicing
# syntax - [start argument : stop argument +1 ]
# lets say if we wanted to print more than one character what we do is we first type sq. brac. and then we write 
# a index number from where we want to print charachters called start argument and put a semicolon : and then type
# a number(add 1 in that number) from where we want to end the character sequence called stop argument
# 0 , -5 = B
# 1 , -4 = i
# 2 , -3 = l
# 3 , -2 = a
# 4 , -1 = l
name = "Bilal"
# always write one number greater than from where you want to end the sequence up.
# if we do not write start argument and stop argument before and after semicolon : respectively interpreter prints full name
print( name[0:3] ) 
# print( name[:] )
# print( name[1:] )        
# print( name[:5] )
# print( name[-5:5] )
# print( name[-4:-2] )
print( name[-4:-1])
# not only a variable we can also print text which is under inverted commas ""
# print( "Bilal"[3] )
