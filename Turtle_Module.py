import turtle               # allows us to use the turtles library
s = turtle.getscreen()
t = turtle.Turtle() # here we create an object of turtle we can create as many object as we want.

# ______________________________________________________________________________________________________________________________________________

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
# t.circle(90,360,5)

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
# turtle.title("My Turtle Program")

# ______________________________________________________________________________________________________________________________________________

# Changing the Turtle Size
# You can increase or decrease the size of the onscreen turtle to make it bigger or smaller. This changes only the 
# of the shape without affecting the output of the pen as it draws on the screen. Try typing in the following commands:
# shapesize has three parameters 
# Parameters
# stretch_wid – positive number
# stretch_len – positive number
# outline – positive number
# t.shapesize(10,12,19)
# t.shapesize(1,5,10)
# t.shapesize(10,5,1)
# t.shapesize(1,10,5)
# t.shapesize(10,1,5)

# ______________________________________________________________________________________________________________________________________________

# Changing the Pen Size
# The previous command changed the size of the turtle’s shape only. However, sometimes, you may need to increase or decrease the thickness of
# your pen. You can do this using the following command:
# t.pensize(100) # pensize or width
# t.circle(200) # we draw circle here just to check the size of pen
# As we can see, the size of your pen is now 100 times the original size (which was one). Try drawing some more lines of various sizes, and 
# compare the difference in thickness between them.

# ______________________________________________________________________________________________________________________________________________

# Changing the Turtle and Pen Color
# When you first open a new screen, the turtle starts out as a black figure and draws with black ink. Based on your requirements, you can do 
# two things:
# Change the color of the turtle: This changes the fill color.
# Change the color of the pen: This changes the outline or the ink color.
# You can even choose both of these if you wish. Before you change the colors, increase the size of your turtle to help you see the color 
# difference more clearly. Type in this code:
# t.shapesize(3,3,3) # we write this here just to make pointer look big so that we can easily watch color changes
# # Now, to change the color of the turtle (or the fill), you type the following:
# t.fillcolor("yellow")
# t.forward(100)

# ______________________________________________________________________________________________________________________________________________

# To change the color of the pen (or the outline), you type the following:
# t.pencolor("red")

# ______________________________________________________________________________________________________________________________________________

# To change the color of both, you type the following:
# t.color("Orange", "red") # first parameter is outline color and second parameter is inside color

# ______________________________________________________________________________________________________________________________________________

# Filling in an Image
# Coloring in an image usually makes it look better, doesn’t it? The Python turtle library gives you the option to add color to your drawings. 
# Try typing in the following code and see what happens:
# t.color("Blue","skyblue") # blue = outer layer , skyblue = inside color
# t.begin_fill()
# t.fd(200)
# t.lt(120)
# t.fd(200)
# t.lt(120)
# t.fd(200)
# t.end_fill()
# When you use .beginfill(), you’re telling your program that you’re going to be drawing a closed shape which will need to be filled in. 
# Then, you use .endfill() to indicate that you’re done creating your shape and it can now be filled in.

# ______________________________________________________________________________________________________________________________________________

# Changing the Turtle Shape
# The initial shape of the turtle isn’t really a turtle, but a triangular figure. However, you can change the way the turtle looks, 
# and you do have a couple of options when it comes to doing so. You can have a look at some of them by typing in the following commands:
# we can use any of these shapes [ “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic” ]
# t.shape("arrow")
# t.shape("turtle")
# t.shape("circle")
# t.shape("square")
# t.shape("triangle")
# t.shape("classic")

# ______________________________________________________________________________________________________________________________________________

# Changing the Pen Speed
# The turtle generally moves at a moderate pace. If you want to decrease or increase the speed to make your turtle move slower or faster, then 
# you can do so by typing the following:
# t.speed(1)
# t.forward(100)
# t.speed(10)
# t.forward(100)
# This code will first decrease the speed and move the turtle forward, then increase the speed and move the turtle forward again
# The speed can be any number ranging from 0 (the slowest speed) to 10 (the highest speed). You can play around with your code to 
# see how fast or slow the turtle will go.
# “fastest”: 0 , “fast”: 10 , “normal”: 6 , “slow”: 3 , “slowest”: 1

# ______________________________________________________________________________________________________________________________________________

# Customizing in One Line
# Suppose you want to set your turtle’s characteristics to the following:
# Pen color: purple , Fill color: orange , Pen size: 10 , Pen speed: 9
# From what you’ve just learned, the code should look something like this:
# t.pencolor("purple")
# t.fillcolor("orange")
# t.pensize(10)
# t.speed(9)
# t.begin_fill()
# t.circle(90)
# t.end_fill()
# # Now, just imagine if you had ten different turtles. Changing all of their characteristics would be extremely tiresome for you to do!.com
# # The good news is that you can reduce your workload by altering the parameters in just a single line of code, like this:
# t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
# t.begin_fill()
# t.circle(90)
# t.end_fill()

# ______________________________________________________________________________________________________________________________________________

# Picking the Pen Up and Down
# Sometimes, you may want to move your turtle to another point on the screen without drawing anything on the screen itself. To do this, you 
# use .penup(). Then, when you want to start drawing again, you use .pendown(). Give it a shot using the code that you used previously to draw
# a square. Try typing the following code:
# t.fd(100)
# t.rt(90)
# t.penup() # commands that we will write under penup will get transparent
# t.fd(100)
# t.rt(90)
# t.pendown() # commands that we will write under penup will show on screen
# t.fd(100)
# t.rt(90)
# t.penup()
# t.fd(100)
# t.pendown()

# ______________________________________________________________________________________________________________________________________________

# Undoing Changes
# No matter how careful you are, there’s always a possibility of making a mistake. Don’t worry, though! The Python turtle library gives you
# the option to undo what you’ve done. If you want to undo the very last thing you did, then type in the following:
# t.undo()
# This undoes the last command that you ran. If you want to undo your last three(or as many commands as you want) commands, then you would 
# type t.undo() three times.

# ____________________________________________________________________________________________________________________________________________

# Clearing the Screen
# Now, you probably have a lot on your screen since you’ve started this tutorial. To make room for more, just type in the following command:
# t.clear() 
# This will clean up your screen so that you can continue drawing. Note here that your variables will not change, and the turtle will remain in
#  the same position. If you have other turtles on your screen other than the original turtle, then their drawings will not be cleared out unless
# you specifically call them out in your code.

# ____________________________________________________________________________________________________________________________________________

# Resetting the Environment
# You also have the option to start on a clean slate with a reset command. The screen will get cleared up, and the turtle’s settings will 
# all be restored to their default parameters. All you need to to do is type in the following command:
# t.reset()
# This clears the screen and takes the turtle back to its home position. Your default settings, like the turtle’s size, shape, color,
# and other features, will also be restored.

# ____________________________________________________________________________________________________________________________________________

# Leaving a Stamp
# You have the option of leaving a stamp of your turtle on the screen, which is nothing but an imprint of the turtle. Try typing in this code 
# to see how it works:
# stamp will return a stamp_id which can be used to delete that stamp later using clearstemp func.
# print(t.stamp()) # id = 8
# t.fd(100)
# print(t.stamp()) # id = 9
# t.fd(100)
# print(t.stamp()) # id = 10
# t.fd(100)
# print(t.stamp())# id = 11
# t.fd(100)

# ____________________________________________________________________________________________________________________________________________

# The numbers that appear are the turtle’s location or stamp ID. Now, if you want to remove a particular stamp, then just use the following:    
# t.clearstamp(10)

# ____________________________________________________________________________________________________________________________________________

# Cloning Your Turtle
# Sometimes, you may need to have more than one turtle on your screen. You’ll see an example of this later on in the final project. For now, you 
# can get another turtle by cloning your current turtle into your environment. Try running this code to create a clone turtle, c, and then move
# both the turtles on the screen:

# c = t.clone()
# t.color("magenta")
# c.color("red")
# t.circle(100)
# c.circle(60)

a = 10
b = "#48C9B0"
for b in range(10):
    t.color("Orange","#48C9B0")
    t.begin_fill()
    t.circle(a)
    t.end_fill()
    a += 5
    t.rt(90)

# t.pensize(20)
# t.circle(100)
# t.speed(3)
# t.rt(90)
# t.fd(70) # R H S
# t.lt(90)
# t.fd(70) # L H S
# t.bk(140)
# t.fd(70)
# t.rt(90)
# t.fd(100)
# t.lt(45)
# t.fd(60)
# t.bk(60)
# t.rt(90)
# t.fd(60)
# t.bk(60)
# t.rt(45)


# for a in range(18):
#     t.speed(0)
#     t.circle(100)
#     t.right(20)

# for a in range(8):
#     t.circle(90,360,5)
#     t.right(45)
#     t.speed(0)


# t.fd(20)
# t.right(20)
# t.fd(100)



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

# for a in range(9):
#     t.speed(0)
#     c = t.clone()
#     c.speed(0)
#     d = c.clone()
#     d.speed(0)
#     t.color("magenta","Orange")
#     c.color("red","pink")
#     d.color("Orange","pink")
#     t.begin_fill()
#     t.circle(100)
#     t.end_fill()
#     c.begin_fill()
#     c.circle(60)
#     c.end_fill()
#     d.begin_fill()
#     d.circle(30)
#     d.end_fill()
#     t.right(45)