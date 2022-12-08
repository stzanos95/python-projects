from turtle import Turtle
import random
import math
from constants import *


def random_velocity():
    return [math.sin(math.radians(random.choice(DIR_ANGLES))),
            math.sin(math.radians(random.choice(DIR_ANGLES)))]


class Ball(Turtle):

    velocity_vector = random_velocity()

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Blue")
        self.penup()
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + self.velocity_vector[0] * MOVE_DISTANCE / 2
        new_y = self.ycor() + self.velocity_vector[1] * MOVE_DISTANCE / 2
        self.goto(new_x, new_y)

    def bounce(self, direction):
        if direction == "x":
            self.velocity_vector[0] *= (-1)
        else:
            self.velocity_vector[1] *= (-1)

    def reset(self):
        self.goto(0, 0)
        self.bounce("x")
