from turtle import Turtle
from random import *
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []

    def car_generator(self):
        rand_chance = randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            rand_y = (randint(-250, 250))
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)

    def Forward(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)




