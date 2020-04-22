import time

# list 
# list takes more memory 
# list takes more time 

t1 = time.time()
l = [ s**2 for s in range(1,11) ]
print(l)
t2 = time.time()
print(t2-t1,"list time")

# generator
# generator takes less memory 
# generator takes less time 

T1 = time.time()
g = ( s**2 for s in range(1,11) )
print(next(g))
T2 = time.time()
print(T2-T1,"generator time")

print((t2-t1)>(T2-T1))