from turtle import Turtle, Screen
from random import *

screen = Screen()
screen.setup(width=500, height=400)
screen.title("turtles_marathon")
user_choice = screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color: ")

turtles = {
    "name":
    ["tim", "jim", "tom", "kim", "lim", "bim"]
    ,
    "color":
    ["red", "cyan", "gray", "orange", "purple", "green"]
               }

turtle_list = []

is_on = True

location = {"x": -230, "y": -60}

for i in range(6):
    turtles["name"] = Turtle()
    turtle_list.append(turtles["name"])
    turtle_list[i].color(turtles["color"][i])
    turtle_list[i].shape("turtle")
    turtle_list[i].penup()
    if i == 0:
        turtle_list[i].goto(x=location["x"], y=location["y"])
    else:
        location["y"] += 30
        turtle_list[i].goto(x=location["x"], y=location["y"])
while is_on:
    for turtle in turtle_list:
        turtle.forward(randint(0,10))
        if turtle.xcor() > 230:
            winner = turtle
            is_on = False

if user_choice == winner.color():
    print("you won!")
else:
    print("you lose")
        
    
screen.exitonclick()
