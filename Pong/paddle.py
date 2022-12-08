from turtle import Turtle
from constants import *


class Paddle(Turtle):

    def __init__(self, player=1):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.penup()
        if player == 1:
            self.goto(PADDLE_X_LEFT, PADDLE_Y)
        else:
            self.goto(PADDLE_X_RIGHT, PADDLE_Y)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y <= MAX_HEIGHT / 2 - (PADDLE_WIDTH / 2) * MOVE_DISTANCE:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y >= -MAX_HEIGHT / 2 + (PADDLE_WIDTH / 2) * MOVE_DISTANCE:
            self.goto(self.xcor(), new_y)
