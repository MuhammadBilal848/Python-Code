# tuple is an other method of storing multiple values in a single variable, there is only one difference b/w tuple and 
# list which is "list elements can be change and we run proper function on list which technically called "Mutable" but 
# in tuple the elements which we store in our variable remains constant which technically called "Immutable" once tuple
# is defined we can use value of it and we can also do slicing, we can't add value in it, we can't remove value from it
# we can make copy of tuple
atuple=("Bilal","Hamza",100,"Araib","Ali")
print(atuple)
# we can also make tuple like this
btuple="Saad","Uzair","Saboor",100
print(btuple)
print(type(btuple))
# we can check index in tuple
print(atuple[2])
# as it is understood that we cannot append,delete,insert any value in tuple.
# atuple.append("Aashir")
# print(atuple) # we will see an error

# The join() method is a string method and returns a string in which the elements of sequence 
# have been joined by str separator.
# Parameters: The join() method takes iterable – objects capable of returning its members one 
# at a time. Some examples are List, Tuple, String, Dictionary and Set
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)