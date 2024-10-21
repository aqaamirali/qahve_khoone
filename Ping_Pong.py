from turtle import Turtle, Screen
from apperance import Board, Ball, Board_Score
from player import Player, Computer
import time

screen = Screen()

screen.bgcolor("blue")
screen.title("***PING_PONG***")
screen.setup(width=800, height=600)

is_on = True

screen.tracer(0)
board = Board_Score()
Board().line()
player = Player()
co_player = Computer()
ball = Ball()
screen.listen()
screen.onkey(player.Up, "Up")
screen.onkey(player.Down, "Down")
screen.onkey(co_player.Up, "w")
screen.onkey(co_player.Down, "s")

t = 0.1

while is_on:
    screen.update()

    time.sleep(t)

    ball.ball_move()
    if ball.xcor() > 350:
        ball.reset_ball()
        t = 0.1
        board.goes_up_c()
    elif ball.xcor() < -350:
        ball.reset_ball()
        t = 0.1
        board.goes_up_p()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit()

    if ball.distance(player.paddle) < 50 and ball.xcor() > 340 or\
            ball.distance(co_player.paddle) < 50 and ball.xcor() < -340:
        ball.x_pos *= -1
        t *= 0.9


screen.exitonclick()