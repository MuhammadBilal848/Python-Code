num1 = int(input("put first number "))
num2 = int(input("put your second number "))
num3 = int(input("put your third number "))
ntotal = num1 + num2 + num3
print( ntotal / 3) 
#  #--------------------------------- OR -----------------------------------
num1 ,  num2 , num3 = input("put your number ").split(",")
ntotal = ( int(num1) + int(num2) + int(num3) ) / 3
print(ntotal) 
#--------------------------------- OR -----------------------------------
num1, num2, num3 = input("put your number ").split(",")
print( f"Arthimatic mean is : {( int(num1) + int(num2) + int(num3) ) / 3 }")