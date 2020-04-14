# Function: function returning function
# this is called first class function or closures functions
def outerfunc():
    def innerfunc():
        print("Hello Pythonista")
    return innerfunc # notice: i didnt put braces here due to which the path of function will return to outer function and whenever i assign 
    # outerfunc in a variable and use print that variable output will be the path of function but when i use braces with that variable it will 
    # become function
var = outerfunc()
print(var) # this will print path of outerfunc
var() # this will print anything present in innerfunc

def to_the_power(p):
    def base(b):
        return b**p # one might think that why base function isn't working when we call to_the_power function the reason is we haven't called the 
    return base # funtion yet 
cube = to_the_power(3)
print(cube(5))