# generators are iterable
# generators have the same sequence as list but generators are not iterable they are iterator
# memory ---- > list [......................] (here this list stores in my memory, when i create this list it will take time to create as well
# as it will occupy more memory)
# memory ---- > generator (.) (generator never generates a complete sequence at once , untill and unless we damand that value from sequence )
# for e.g. if i want one value from my generator gen(1) it will generate that value and return it to me and if i want second value gen(2) it will
# delete previous value and generate my second value and return it to me and that gives us memory and time saving benefit
 
# now lets create generator
# so here i define function that takes a number as argument and function will generate numbers 
def nums(n):
    for a in range(1,n+1):
        yield a   # here "yield" creates generator and  help us to generate numbers and as mentioned above that generators are iterators 
        # so this function will return an iterator
a = nums(10)
print(a) # so this is an iterator and we can only loop over an iterator one time not if when we convert it in list,tuple etc
print(next(a)) # at this point yields generate 1
print(next(a)) # at this point yield deletes 1 and generate 2
print(next(a)) # at this point yield deletes 2 and generate 3
print(next(a)) # at this point yield deletes 3 and generate 4
print(next(a)) # at this point yield deletes 4 and generate 5
print(next(a)) # at this point yield deletes 5 and generate 6
print(next(a)) # at this point yield deletes 6 and generate 7
print(next(a)) # at this point yield deletes 7 and generate 8
print(next(a)) # at this point yield deletes 8 and generate 9
print(next(a)) # at this point yield deletes 9 and generate 10
print(next(a,"stop iteration"))

# now here is a example to create generator function that return even numbers
def even_num_gen(n):
    for b in range(1,n+1):
        if b%2==0:
            yield b
        else:
            continue
f = even_num_gen(9)
print(next(f))
print(next(f))
print(next(f))
print(next(f))


