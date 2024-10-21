from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 0.3
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.seth(90)

    def move(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

