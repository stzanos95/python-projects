from turtle import Turtle
from constants import *


class GameTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(TURTLE_COLOR)
        self.penup()
        self.goto(0, -SCREEN_SIZE_Y / 2 + TURTLE_SIZE)
        self.left(90)

    def move_up(self):
        self.forward(TURTLE_MOVEMENT)

    def reset_pos(self):
        self.goto(0, -SCREEN_SIZE_Y / 2 + TURTLE_SIZE)
