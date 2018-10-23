# our first class
from random import *
import turtle

class msdie:
    t = turtle
    
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
        
# code to test if this is working
die1 = msdie(6)
die1.roll()


if die1.getValue() == 4:
    die1.drawSide4()
    
if die1.getValue() ==5:
die1.side5(200, 20)

print("die value is: ", die1.getValue())
