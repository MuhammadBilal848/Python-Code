a=int(input("How many times you want to run this code: "))
alist=[]
for b in range(a):
    b=input("Enter your number: ")
    alist.append(int(b))
print(f"List of numbers that you entered is: {alist}")
alist.sort(reverse=False)
print(f"Your entered number in ascending order: {alist}")
popped_elm=alist.pop()
print(f"Greatest number in your list is: {popped_elm}")        