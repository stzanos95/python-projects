from turtle import Screen
import time
from constants import *
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball


if __name__ == "__main__":
    # Setup screen
    screen = Screen()
    screen.setup(MAX_WIDTH, MAX_HEIGHT)
    screen.title(PONG_TITLE)
    screen.bgcolor(BACKCOL)
    scoreboard = Scoreboard()
    screen.tracer(0)

    # Initialize objects
    paddle_l = Paddle(player=1)
    paddle_r = Paddle(player=2)
    ball = Ball()

    # Game start
    screen.listen()

    # Players' movements
    screen.onkey(paddle_l.move_up, "w")
    screen.onkey(paddle_l.move_down, "s")
    screen.onkey(paddle_r.move_up, "Up")
    screen.onkey(paddle_r.move_down, "Down")

    while True:
        screen.update()
        time.sleep(0.05)
        if MAX_HEIGHT / 2 - BOUNCE_DB >= ball.ycor() >= - MAX_HEIGHT / 2 + BOUNCE_DB:
            if ball.xcor() <= PADDLE_X_LEFT + BOUNCE_DB:
                if ball.distance(paddle_l.xcor(), paddle_l.ycor()) <= PADDLE_WIDTH * BOUNCE_DB / 2:
                    ball.bounce("x")
                else:
                    ball.reset()
                    scoreboard.goal_scored(2)
            elif ball.xcor() >= PADDLE_X_RIGHT - BOUNCE_DB:
                if ball.distance(paddle_r.xcor(), paddle_r.ycor()) <= PADDLE_WIDTH * BOUNCE_DB / 2:
                    ball.bounce("x")
                else:
                    ball.reset()
                    scoreboard.goal_scored(1)
        else:
            ball.bounce("y")
        ball.move()

    # Background
    screen.exitonclick()
