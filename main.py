from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_over = False
speed = 0.1

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_over is False:
    screen.update()
    time.sleep(speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if ball.xcor() >= r_paddle.xcor() - 20 and ball.distance(r_paddle) < 55 or ball.xcor() <= l_paddle.xcor() + 20 and ball.distance(l_paddle) < 55:
        ball.bounce_paddle()
        speed *= 0.8
    if ball.xcor() > 380:
        scoreboard.l_score += 1
        scoreboard.update_score()
        r_paddle.reset_paddle((350, 0))
        l_paddle.reset_paddle((-350, 0))
        ball.reset_ball()
        speed = 0.1
    if ball.xcor() < -380:
        scoreboard.r_score += 1
        scoreboard.update_score()
        r_paddle.reset_paddle((350, 0))
        l_paddle.reset_paddle((-350, 0))
        ball.reset_ball()
        speed = 0.1

screen.exitonclick()
