import turtle
import random

wn = turtle.Screen()
wn.title("Circle Fun")

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
t.color("red")

for angle in range (0, 360, 15):
    t.seth(angle)
    t.circle(100)

wn.exitonclick()