name = "      Bi   lal      "
dots = ".................."
print( name + dots )
#  if we want to remove the left or right space of a string we use strip method
print( name.lstrip() + dots ) # it removes left space 
print( name.rstrip() + dots ) # it removes right space
# if we want to remove spaces completely from a string we use only strip()
print( name.strip() + dots )
# strip function cannot remove those space which are between the string character
# name = "      Bilal      "
# output :       Bilal      
# spaces b/w string characters can be removed by using replace function
print( name.replace(" ","" ) + dots) # "space part" ,(replaces by) "" 