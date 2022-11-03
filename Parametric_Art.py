#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Catherine Xie
'''

# My artpiece is that of the Fibonacci Spiral, a visual representation of the golden ratio.
# A user can chose how many sequeneces for the spiral, but it is limited to 6. 
# The squares are drawn with black, and the spiral red to visually stand out.

import turtle
import math

# equation from https://www.codingninjas.com/codestudio/library/plot-fibonacci-spiral-fractal-using-turtle-in-python
def fiboPlot(n):
   a = 0
   b = 1
   sqr_a = a
   sqr_b = b

   # Setting the color of the plotting pen to orange
   y.pencolor("black")
   y.pensize(3)

   # Drawing the first sqr
   y.forward(b * fac)
   y.left(90)
   y.forward(b * fac)
   y.left(90)
   y.forward(b * fac)
   y.left(90)
   y.forward(b * fac)

   # Proceeding in the Fibonacci Series
   temp = sqr_b
   sqr_b = sqr_b + sqr_a
   sqr_a = temp
  
   # Drawing the rest of the sqrs
   for i in range(1, n):
       y.backward(sqr_a * fac)
       y.right(90)
       y.forward(sqr_b * fac)
       y.left(90)
       y.forward(sqr_b * fac)
       y.left(90)
       y.forward(sqr_b * fac)

       # Proceeding in the Fibonacci Series
       temp = sqr_b
       sqr_b = sqr_b + sqr_a
       sqr_a = temp

   # Bringing the pen to starting point of the spiral plot
   y.penup()
   y.setposition(fac, 0)
   y.seth(0)
   y.pendown()

   # Set the color of the plotting pen to red
   y.pencolor("red")

   # Fibonacci Spiral Plot
   y.left(90)
   for i in range(n):
       print(b)
       fdwd = math.pi * b * fac / 2
       fdwd /= 90
       for j in range(90):
           y.forward(fdwd)
           y.left(1)
       temp = a
       a = b
       b = temp + b

t = input("Input how many Fibonacci iterations:")
t = int(t)
fac = t

if t > 6:
    exit

else:
    y = turtle.Turtle()
    y.speed(50)
    fiboPlot(10)
    turtle.done()