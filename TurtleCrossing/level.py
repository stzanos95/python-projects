from turtle import Turtle
from constants import *


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.difficulty = 1
        self.max_difficulty = 20
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.goto(-SCREEN_SIZE_X / 2 + 50, SCREEN_SIZE_Y / 2 - OFFSET_FINISH)
        self.update_header()

    def update_header(self):
        self.clear()
        self.write("Level: {}".format(self.difficulty), align=HEADER_ALIGN, font=HEADER_FONT)

    def next(self):
        self.difficulty += 1
        self.update_header()

    def game_over(self):
        self.color("Black")
        self.goto(0, 0)
        self.write("GAME OVER", align=HEADER_ALIGN, font=GAMEOVER_FONT)
