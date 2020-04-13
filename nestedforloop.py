# Nested loop means loop inside loop.
for a in range(5):
    print("Inner loop begins")
    for char in "Karachi":
        print(a, char)
# write a program which takes input from a user in form of integer and automatically generate table of given number.
# TableNum=int(input("Type a number: "))
# for a in range(1,11):
#     print(f"{TableNum} * {a} = {TableNum * a} ")
#    ********_______________*******
tables=int(input("Type table number which you want: "))
for table in range(1,tables+1):
    for num in range(1,11):
        print(f"{table} x {num} = {table * num}")