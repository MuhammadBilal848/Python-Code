# set is an unordered collection of items
# set syntax
# variable = {item1,item2,item2,....}
# we cant store list and dictionary in set and cant store set it self

s = {1,2,3}
print(s)
# in set's defn unique means if any item is repeated it does not show as output in set
s = {1,2,3,4,3,4,2,1} # set dont have duplicates
print(s)
# in set's defn unordered collection means there is no indexing in sets
# this is not necessary that if items in set are unordered so our set print it in ascending order thats not true(its some times may or may not)
s = {1,2,3} 
print(s)
s = {1,1.1,2.3,"String"}
print(s)
# print(s[2]) # this will generate error because there is no indexing in sets
# if want to give 
l =  [1,2,3,4,5,6,7,2,2,3,3,4,5,5,7,7,7,6,6,6]
a = set(l) # now this became a list but if we want to convert it in list we again use list function
print(a) 
# convert set to list
la =  [1,2,3,4,5,6,7,2,2,3,3,4,5,5,7,7,7,6,6,6]
a = list(set(la)) # now this became a list but if we want to convert it in list we again use list function
print(a)
# we can also store anykind of data type in our set
b = {1,2,3,"one","two","three"}
print(b)
################################# METHODS OF SETS #########################################
# if we want to add item in sets we use add method
print("                                   add()")
s = {1,2,3,4,5,6}
s.add(7)
print(s,"added 7")
#################################################################################
# if we want to remove items in our set we use remove method
# Remove an element from a set; it must be a member
# If the element is not a member, raise a KeyError
print("                                   remove()")
s = {1,2,3,4,5,6}
s.remove(4)
print(s,"removed 4")
#################################################################################
# if we want to remove items in our set such that if its not present so method does not give error
# we use discard method for this 
print("                                   discard()")
s = {1,2,3,4,5,6}
s.discard(4)
print(s,"discard 4")
s.discard(9) # since 9 isnot present in the set so it doesnt give error
print(s,"discard 9")
#################################################################################
# if we want to make copy of our set we use copy method which works same as list and dictionary 
print("                                   copy()")
s = {1,2,3,4,5,6}
a = s.copy()
print(a)
a.add(7)
print(a)                   # by value
print(s)

s = {1,2,3,4,5,6}
b = s
print(b)
b.add(7)
print(b)                # by reference
print(s)
#################################################################################
# You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered,
# so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.
print("                                   pop()")
s = {1,2,3,4,5,6}
b = s.pop()
print(b)
print(s)
#################################################################################
# The clear() method empties the set.
print("                                   clear()")
s = {1,2,3,4,5,6}
s.clear()
print(s)
##############################################################################
# The del keyword will delete the set completely
print("                                    del keyword")
s = {1,2,3,4,5,6}
del s
# print(s) # this will delete list completely
##############################################################################
# he update() method updates the current set, by adding items from another set.
# If an item is present in both sets, only one appearance of this item will be present in the updated set.
# this has one parameter named "set" (Required. The set insert into the current set)
print("                                   update()")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x)
print(y)
x.update(y)
print(x)
##############################################################################
# The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.
# this has one parameter named "set" (Required. The set insert into the current set)
print("                                   difference()")
a = {1,2,3,4,5,6,7}
b = {1,5,4,3,6,8}
c = a.difference(b)
print(c)
##############################################################################
# The difference_update() method removes the items that exist in both sets.
# The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the
# unwanted items, and the difference_update() method removes the unwanted items from the original set.
print("                                   difference_update()")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"} 
x.difference_update(y) # so here apple is same in both sets thats why this method removes this and return a new set
print(x)
#  this has one parameter named "set" (Required. The set to check for differences in both)
##############################################################################
# The intersection() method returns a set that contains the similarity between two or more sets.
# Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.
# this has arguemnts (set1,set2,,...)
# set1	Required. The set to search for equal items in
# set2	Optional. The other set to search for equal items in.
# You can compare as many sets you like.
# Separate the sets with a comma
# syntax set.intersection(set1, set2 ... etc)
print("                                   intersection()")
a = {1,2,3,4,5,6}
b = {5,6,7,4,8,5,6}
c = a.intersection(b)
print(c)
# ________OR__________
a = {1,2,3,4,5,6}
b = {5,6,7,4,8,5,6}
c1 = a & b
print(c1)
##############################################################################
# The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more 
# than two sets). means it will return all common items from all sets
# The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without 
# the unwanted items, and the intersection_update() method removes the unwanted items from the original set.
# this has arguemnts (set1,set2,,...)
# set1	Required. The set to search for equal items in
# set2	Optional. The other set to search for equal items in.
# You can compare as many sets you like.
# Separate the sets with a comma
print("                                   intersection_update()")
a = {1,2,3,4,5,6}
b = {5,6,7,4,8,5,6,1}
a.intersection_update(b)
print(a )

a = {1,2,3,4,5,6}
b = {5,6,7,4,8,5,6,1}
c = {1,2,3,4,5,6,7}
a.intersection_update(b,c)
print(a)
##############################################################################
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
# disjoint - two sets are said to be disjoint sets if they have no element in common
# this has one parameter named "set" (Required. The set insert into the current set)
# syntax set.isdisjoint(set)
print("                                   isdisjoint()")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) 
print(z)
# _____________OR___________________
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)
##############################################################################
# The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
# this has one parameter named "set" (Required. The set insert into the current set)
# syntax set.issubset(set)
print("                                   issubset()")
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
# _____________OR___________________
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)
##############################################################################
# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
# this has one parameter named "set" (Required. The set insert into the current set)
# syntax set.issuperset(set)
print("                                   issuperset()")
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
# _____________OR__________________
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
##############################################################################
# The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
# Meaning: The returned set contains a mix of items that are not present in both sets.
# syntax - set.symmetric_difference(set)
# this has one parameter named "set" (Required. The set insert into the current set)
print("                                   symmetric_difference()")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
##############################################################################
# The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
# syntax - set.symmetric_difference_update(set)
# this has one parameter named "set" (Required. The set insert into the current set)
print("                                   symmetric_difference_update()")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
##############################################################################
# The union() method returns a set that contains all items from the original set, and all items from the specified sets.
# You can specify as many sets you want, separated by commas
# If an item is present in more than one set, the result will contain only one appearance of this item.
# syntax - set.union(set1, set2...)
# set1	Required. The set to unify with
# set2	Optional. The other set to unify with.
# You can compare as many sets as you like.
# Separate each set with a comma
print("                                  Union()")
a = {1,2,3,4}
b = {5,6,7,8}
c = a.union(b)
print(c)
# _____________OR__________________
a = {1,2,3,4}
b = {5,6,7,8}
union = a | b
print(union)