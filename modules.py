import turtle               # allows us to use the turtles library
s = turtle.getscreen()
t = turtle.Turtle() # here we create an object of turtle we can create as many object as we want
t.color("green")
# t.forward(150) # forward or fd (move turtle pointer forwards) (takes one argument as distance)

# ______________________________________________________________________________________________________________________________________________

# t.right(90) # right or rt (turn turtle right by angle units) (takes one argument as angle)
# ______________________________________________________________________________________________________________________________________________

# t.backward(150) # backward or bk (move turtle pointer backwards) (takes one argumnt as distance)

# ______________________________________________________________________________________________________________________________________________

# t.left(90) # left or lt (turn turtle left by angle units) (takes one argument as angle)

# ______________________________________________________________________________________________________________________________________________

# we can also draw a circle using circle method
# # this takes three parameters (radius, extent=None, steps=None) 
# # here extent is an angle which will decide at what angle our pointer needs to stop.(circle takes 360 degrees to complete so extent will decide
# # at what angle we need to stop circle from making, here in line no 8 i have given 350 degrees that means it will stop just before 10 degrees of
# # completing circle)
# # here steps will help us to create other polygons from circle in shot we pass sides of any shape in step(like triangle has 3 sides,rectangle
# # has 4,pentagon has 5 etcc)
t.circle(90,360,5)

# ______________________________________________________________________________________________________________________________________________

# you can also draw a dot, which is nothing but a filled-in circle. first parameter is dot size and second is color
# we can pass color name as well as hex code of color
# [ #3498DB , #F1C40F , #48C9B0 , #AAB7B8 , #7F8C8D , #E74C3C , #17202A , #1ABC9C  , #AEB6BF     ]
# t.dot(500,"#AEB6BF")
# t.dot(500,"#1ABC9C")
# t.dot(500,"#17202A")
# t.dot(500,"#E74C3C")
# t.dot(500,"#7F8C8D")
# t.dot(500,"#AAB7B8")
# t.dot(500,"#48C9B0")
# t.dot(500,"#F1C40F")
# t.dot(500,"#3498DB")
# t.dot(500,"yellow")

# ______________________________________________________________________________________________________________________________________________

# Changing the Screen Color
# By default, turtle always opens up a screen with a white background. However, you can change the color of the screen at any time using
# the following command:
# turtle.bgcolor("#48C9B0")
# we can pass color name as well as hex code of color in form of string
# [ #3498DB , #F1C40F , #48C9B0 , #AAB7B8 , #7F8C8D , #E74C3C , #17202A , #1ABC9C  , #AEB6BF     ]

# ______________________________________________________________________________________________________________________________________________

# Changing the Screen Title
# Sometimes, you may want to change the title of your screen. You can make it more personal, like "My Turtle Program", or more suitable
# to what you’re working on, like "Drawing Shapes With Turtle". You can change the title of your screen with the help of this command:
t1 = turtle.Turtle()
for a in range(18):
    t1.speed(0.5)
    t1.circle(100)
    t1.right(20)

# ninja = turtle.Turtle()
# turtle.bgcolor("yellow")
# ninja.color("green")
# ninja.speed(0)

# for i in range(180):
#     ninja.forward(100)
#     ninja.right(30)
#     ninja.forward(20)
#     ninja.left(60)
#     ninja.forward(50)
#     ninja.right(30)
    
#     ninja.penup()
#     ninja.setposition(0, 0)
#     ninja.pendown()
    
#     ninja.right(2)
    
# turtle.done()



# To move the turtle to any other area on the screen, you use .goto() and enter the coordinates like this:
# t.goto(50,45) 
# t.home() # bring the turtle back to its home position 
# t.backward(100)
# t.forward(100)
# t.right(90)
# t.backward(100)
# t.left(90)
# t.forward(100)
# t.right(90)
# t.backward(100)
# turtle.bgcolor("Green")
# t.color("Yellow") # change the pointeer color
# turtle.title("titlestring")
# t.circle(109)
# for a in range(4):
#     t.forward(150) # / forward or fd
#     t.right(90)
# t.fd(150) # backward or back or bk
# t.right(90) # right or rt
# t.left(90) # left or lt
# t.fd(150)
# t.right(90)
# t.fd(150)

input("Press any key to exit ...")
# t.right(90)
# t.forward(100)
# t.left(90)
# t.backward(100)

# # wn = turtle.Screen()        # creates a graphics window
# alex = turtle.Turtle()      # create a turtle named alex
# alex.forward(800)           # tell alex to move forward by 150 units
# alex.left(450)               # turn by 90 degrees
# alex.forward(750)            # complete the second side of a rectangle


# import turtle 

# spiral = turtle.Turtle()

# for i in range(20):
#     spiral.forward(i * 10)
#     spiral.right(144)
    
# turtle.done()

# import turtle 

# painter = turtle.Turtle()

# painter.pencolor("blue")

# for i in range(50):
#     painter.forward(50)
#     painter.left(123) # Let's go counterclockwise this time 
    
# painter.pencolor("red")
# for i in range(50):
#     painter.forward(100)
#     painter.left(123)
    
# turtle.done()


# ninja = turtle.Turtle()

# ninja.speed(10)

# for i in range(180):
#     ninja.forward(100)
#     ninja.right(30)
#     ninja.forward(20)
#     ninja.left(60)
#     ninja.forward(50)
#     ninja.right(30)
    
#     ninja.penup()
#     ninja.setposition(0, 0)
#     ninja.pendown()
    
#     ninja.right(2)
    
# turtle.done()
# turtle.done()