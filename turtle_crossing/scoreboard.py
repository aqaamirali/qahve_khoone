from turtle import Turtle
from player import Player
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.starting_score = 0
        self.player = player

    def end_game(self):
        self.goto(x=0, y=0)
        self.write("Game Over.", True, "center", FONT)

    def score(self):
        self.goto(x=-250, y=250)
        self.clear()
        self.write(f"Level:{self.starting_score} ", True, "center", ("Courier", 14, "normal"))

    def call_score(self):
        self.starting_score += 1
        self.player.setpos(0, -280)

