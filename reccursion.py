import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
a = 1
def name():
    global a
    a += 1
    print("Hello Pythonsitas",a)
    name()
name()