from turtle import Turtle
from constants import *


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update()

    def update(self):
        self.clear()
        self.write("{} - {}".format(self.score[0], self.score[1]), align=ALIGNMENT, font=FONT)

    def goal_scored(self, player):
        if player == 1:
            self.score[0] += 1
        else:
            self.score[1] += 1
        self.update()

