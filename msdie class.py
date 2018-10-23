# our first class
from random import *


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

    def drawSide4(self):
        import turtle
        t = turtle
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

# code to test if this is working
die1 = msdie(6)
die1.roll()
# if die1.getValue() == 4:
die1.drawSide4()

print("die value is: ", die1.getValue())

#check if the dice side is 2
if die1.getValue() == 2:

    #if so, import the turtle module
    import turtle

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
    turtle.exitonclick()

