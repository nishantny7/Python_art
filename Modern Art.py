from turtle import *
import random
from random import randint
color=["red","green","blue","orange","purple","pink","yellow"]
t=Turtle()
t.shape("turtle")
t.speed(13)

def randomcolor(t):
  colour=random.choice(color)
  t.color(colour)
  
def randomplace(t):
  t.penup()
  x=randint(-100,100)
  y=randint(-100,100)
  t.goto(x,y)
  t.pendown()
  
def randomheading(t):
  number=randint(1,360)
  t.setheading(number)

def drawrectangle(t):
  randomcolor(t)
  randomplace(t)
  t.hideturtle()
  length = randint(10, 100)
  height = randint(10, 100)
  t.begin_fill()
  t.forward(length)
  t.right(90)
  t.forward(height)
  t.right(90)
  t.forward(length)
  t.right(90)
  t.forward(height)
  t.right(90)
  t.end_fill()
  
def drawcircle(t):
  randomcolor(t)
  randomplace(t)
  t.hideturtle()
  radius=randint(10,100)
  t.dot(radius)
  
def drawstar(t):
  randomcolor(t)
  randomplace(t)
  t.hideturtle()
  t.begin_fill()
  for i in range(5):
    t.left(144)
    t.forward(50)
  t.end_fill()
  

for i in range(50):
  randomcolor(t)
  randomplace(t)
  randomheading(t)
  t.stamp()

t.clear()
t.setheading(0)
t.speed(20)

for i in range(20):
  drawrectangle(t)

t.clear()

for i in range(50):
   drawcircle(t)
  
t.clear()
t.speed(0)

for i in range(30):
  drawstar(t)