# we use exception handling in python when we expect some sort of unexpected output
# age = int(input("Enter your age here: "))
# if age>=18:
#     print("Yes you can play")
# else:
#     print("You can't play")
# in the above code user input a number(integer) to know whether he is underage or not 
# what if user give input in string format(seven,eight,.........)
# interpretor will give error so here we use exception handling to overcome this problem
# first we have to decide which line can cause error
# and the line which cause error we write that line in try's block
while True:
    try:
        age = int(input("Enter your age here: "))
        break # when ever user input right value(int), break will be executed
# we can write multiple lines of code in try's block as per requirement 
# if any anyline of code generate error in this block interpretor will not execute those lines it just works as "if"
    except ValueError: # here we can also use valueError because we are supposing that here must be a value error
# in python as any other languages we should only handle those exceptions which we think can generate a error
# this will save time of interpretor not to search in libraries or classes to find which error is that
        print("Invalid Input...................")
# if the expected error isn't a ValueError we will write another exception 
    except:
        print("Unexpected Error") # all those exce. which are not valueerror, handeled by this exception
# we can write multiple lines of code in try's block as per requirement 
# when the code present in try's block generate error except block will execute it just works as "else"
# python uses another keyword in exception handling "Else", if try block successfully executed interpretor directly
# execute else block in other words if try block wont have any exception else block will execute  
    else:
        if age>=18: # here indentation is not important because "age" variable will form already from try's block
            print("Yes you can play")
        else:
            print("You can't play")
# now we have another keyword "Finally", finally's block will always execute whether the code in try's block has exception or not
    finally:
        print("Finally is executed")