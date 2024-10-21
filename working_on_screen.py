from turtle import Turtle, Screen
from random import *
timmy = Turtle()
colors = ["black", "red", "orchid", "blue", "green", "brown", "violet", "purple"]
timmy.speed(0)
rad = 360
x = True
while x:
    timmy.color(choice(colors))
    timmy.circle(100)
    rad -= 5
    timmy.seth(rad)
    if rad == 0:
        x = False

screen = Screen()
screen.exitonclick()
