# our first class
from random import *
import turtle
t = turtle

class msdie:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)
        return self.value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
    def one_dot():
        for x in range(4):
            t.forward(100)
            t.right(90)
        for x in range(4):
            t.penup()
            t.goto(50, -50)
            t.dot(10, "Black")
            t.pendown    
    def side3():
        #Set the starting position for the drawing of the square
        t.penup()
        t.setpos(-200,200)
        t.pendown()

                # Drawing the four sides of the square shaped size
        for i in range(4):
            t.forward(400)
            t.right(90)
        t.penup()
        t.setpos(-100,70)
        t.dot(30)
        t.setpos(0, -30)
        t.dot(30)
        t.setpos(100,-130)
        t.dot(30)
        t.done()
        t.exitonclick()
    def drawSide4(self):

        t.penup()
        t.setpos(-100, 100)
        t.pendown()
        for i in range(4):
            t.forward(200)
            t.right(90)
        t.penup()
        t.setpos(-35, 35)
        t.pendown()
        t.dot(25)
        t.penup()
        t.setpos(-35, -35)
        t.pendown()
        t.dot(25)
        t.penup()
        t.setpos(35, 35)
        t.pendown()
        t.dot(25)
        t.penup()
        t.setpos(35, -35)
        t.pendown()
        t.dot(25)
        t.exitonclick()
   def side5(self, size, dotsize):
        t = turtle
        t.setposition(0, 0)
        t.hideturtle()
        for x in range(0, 4):  # loop so it draws 4 sides
            t.forward(size)  # side
            t.right(90)  # corner
        t.penup()
        t.setposition(size/4, -size/4)  # first dot
        t.pendown()
        t.dot(dotsize)  # draw dot
        t.penup()
        t.setposition(size/4*3, -size/4)
        t.pendown()
        t.dot(dotsize)
        t.penup()
        t.setposition(size/2, -size/2)
        t.pendown()
        t.dot(dotsize)
        t.penup()
        t.setposition(size/4, -size/4*3)
        t.pendown()
        t.dot(dotsize)
        t.penup()
        t.setposition(size/4*3, -size/4*3)
        t.pendown()
        t.dot(dotsize)
        t.exitonclick()
die1 = msdie(6)
die1.roll()
if die1.getValue() == 1:
    die1.one_dot()
#check if the dice side is 2
if die1.getValue() == 2:

    #set the background color to yellow. and hide turtle
    turtle.bgcolor("yellow")
    turtle.hideturtle()

    #begin the fillinf process, making the color white
    turtle.fillcolor("white")
    turtle.begin_fill()

    #draw the four sides
    for i in range (4):
        turtle.forward (90)
        turtle.left(90)

    #fill the square made
    turtle.end_fill()

    for z in range (die1.getValue()):
        #lift the pen up
        turtle.penup()

        #go to the given x,y coordinates
        turtle.goto(x,y)

        #put the pendown
        turtle.pendown()

        #make a 10 pixel wide black dot
        turtle.dot(10,"black")

        #add 40 to the coordinates
        x += 40
        y += 40

 #exit the window when the user clicks the screen
if die1.getValue() == 3:
    die1.side3()
if die1.getValue() == 4:
    die1.drawSide4()
if die1.getValue() == 5:
    die1.side5(25, 25)
if die1.getValue() == 6:
    t.screensize(500, 500)
    t.speed(4)
    t.penup()   # not drawing when moving
    t.setpos(-100, 100)  # setting up the start position
    t.pendown()   # drawing when moving
    for i in range(4):    # drawing the frame of the dice ( a square )
        t.forward(200)
        t.right(90)
    def draw_dots():
        t.penup()
        t.setposition(-40, 60)  # drawing the first column of the dots
        t.setheading(-90)
        t.pendown()
        t.dot(30,"blue")
    for i in range(2):
        t.penup()
        t.forward(60)
        t.pendown()
        t.dot(30, "blue")
    t.penup()
    t.setposition(35, 60)   # drawing the second column of the dots
    t.setheading(-90)
    t.pendown()
    t.dot(30, "blue")
   for i in range(2):
       t.penup()
       t.forward(60)
       t.pendown()
       t.dot(30, "blue")
   draw_dots()

t.hideturtle() # make the turtle invisible
t.exitonclick() # quit when we choose

# code to test if this is working
print("die value is: ", die1.getValue())
