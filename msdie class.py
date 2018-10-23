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

# code to test if this is working
die1 = msdie(6)
die1.roll()
if die1.getValue() == 1:
    die1.one_dot()
elif die1.getValue() == 4:
    die1.drawSide4()

print("die value is: ", die1.getValue())
