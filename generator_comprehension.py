# generator comprehension - with the help of this we can create generator in single line
gen = [ (yield a**2) for a in range(1,11) ] # so this is list comprehension not genrator comp. , we can do make generator in this way too but
# this will not return generator iterator this will return a list iterator
print(gen) # this will return a list object
print(next(gen))
print(next(gen))
print(next(gen))
# we can do this in another way which is professional and will return generator iterator
gen1 = ( i**2 for i in range(1,11) ) # this will return generator iterator
print(gen1)
print(next(gen1))
print(next(gen1))
print(next(gen1))

gen2 = ( i**2 for i in range(1,11) if i%2==0 ) 
print(gen2)
print(next(gen2))
print(next(gen1))
print(next(gen1))
print(next(gen1))
