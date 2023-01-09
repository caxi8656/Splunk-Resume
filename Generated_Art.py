#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Catherine Xie
'''

# For my artpiece, there will be two sets of five different colors of circles that will be
# in randomly generated places. The color of the circles it based on IBM's color palette for 
# the colorblind. There will also be three stagnant black circles in the front.

import turtle # import the library of commands that you'd like to use
import random 
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 

#====================================================== Your code ======================================================

color = ["#648FFF", "#785EF0", "#DC267F", "#FE6100", "#FFB000"]
range = (-300, 300)
zeroRange = (-250, 250)
oneRange = (-200, 200)
twoRange = (-100, 100)
threeRange = (-75, 75)
fourRange = (-60, 60)

x = random.randint(-350, 350)
y = random.randint(-350, 350)

for x in range:
    hopper = turtle.Turtle()
    hopper.goto(x, y)
    print(hopper.xcor(), hopper.ycor())
    hopper.color(color[0])
    hopper.begin_fill()
    hopper.circle(200)
    hopper.end_fill()

    if x in zeroRange:
        break

x = random.randint(-300, 300)
y = random.randint(-300, 300)

for x in zeroRange:
    hopper = turtle.Turtle()
    hopper.goto(x, y)
    print(hopper.xcor(), hopper.ycor())
    hopper.color(color[1])
    hopper.begin_fill()
    hopper.circle(175)
    hopper.end_fill()

    if x in oneRange:
        break

x = random.randint(-250, 250)
y = random.randint(-250, 250)

for x in oneRange:
    hopper = turtle.Turtle()
    hopper.goto(x, y)
    print(hopper.xcor(), hopper.ycor())
    hopper.color(color[2])
    hopper.begin_fill()
    hopper.circle(150)
    hopper.end_fill()

    if x in twoRange:
        break

x = random.randint(-100, 100)
y = random.randint(-100, 100)

for x in twoRange:
    hopper = turtle.Turtle()
    hopper.goto(x, y)
    print(hopper.xcor(), hopper.ycor())
    hopper.color(color[3])
    hopper.begin_fill()
    hopper.circle(125)
    hopper.end_fill()

    if x in threeRange:
        break

x = random.randint(-75, 75)
y = random.randint(-75, 75)

for x in threeRange:
    hopper = turtle.Turtle()
    hopper.goto(x, y)
    print(hopper.xcor(), hopper.ycor())
    hopper.color(color[4])
    hopper.begin_fill()
    hopper.circle(100)
    hopper.end_fill()

    if x in fourRange:
        break

circle = turtle.Turtle()
circle.shape("circle")
circle = turtle.forward(100)
turtle.color("black")
turtle.begin_fill()
turtle.circle(150)
turtle.end_fill()

turtle.goto(-100, -100)
turtle.color("black")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.goto(100, -300)
turtle.color("black")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!
