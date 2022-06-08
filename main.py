from turtle import Screen
from racket import Racket
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("                                                                                       "
             "                        P O N G")
screen.tracer(0.5)
screen.listen()

game_is_on = True

rackets = Racket()
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(rackets.right_move_up, "Up")
screen.onkey(rackets.right_move_down, "Down")
screen.onkey(rackets.left_move_up, "w")
screen.onkey(rackets.left_move_down, "s")

while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()
    elif ball.distance(rackets.right_body) < 50 and ball.xcor() > 370 or \
            ball.distance(rackets.left_body) < 50 and ball.xcor() < -370:
        ball.racket_bounce()
    elif ball.xcor() > 420:
        scoreboard.increase_l_score()
        ball.reset()
    elif ball.xcor() < -420:
        scoreboard.increase_r_score()
        ball.reset()
screen.exitonclick()
