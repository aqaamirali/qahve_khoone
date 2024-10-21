import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle_Crossing")
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard(player)
screen.listen()
is_moving = False


def enable_movement():
    global is_moving
    is_moving =True


def disable_movement():
    global is_moving
    is_moving = False


screen.onkeypress(enable_movement, "w")
screen.onkeyrelease(disable_movement, "w")
game_is_on = True
t = time.time()
while game_is_on:
    screen.update()
    score_board.score()
    c = time.time()
    if is_moving:
        player.move()
    if c - t > 0.1:
        car_manager.car_generator()
        car_manager.Forward()
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                score_board.end_game()
                game_is_on = False
        t = c
    if player.ycor() > 280:
        score_board.call_score()

screen.exitonclick()
