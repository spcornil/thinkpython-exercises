################
# Exercise 4-2 #
################
# Write an appropriately general set of functions that can draw flowers as in Figure 4-1

import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n)
    
def move(t, dist):
    t.pu()
    t.fd(dist)
    t.pd()

bob = turtle.Turtle()

move(bob, -150)
flower(bob, 7, 60, 60)
move(bob, 150)
flower(bob, 10, 40.0, 80.0)
move(bob, 150)
flower(bob, 20, 140.0, 20.0)

turtle.mainloop()