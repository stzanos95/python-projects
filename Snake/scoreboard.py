from turtle import Turtle
from os.path import exists
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


def get_highscore():
    if exists("highscore.log"):
        with open("highscore.log") as f:
            return int(f.read())
    else:
        return 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = get_highscore()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write("Score: {}  Highscore: {}".format(self.score, self.highscore), align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def increase_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.clear()
            self.update_scoreboard()
            self.save_highscore()

    def reset_score(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()

    def save_highscore(self):
        with open("highscore.log", "w") as f:
            f.write(str(self.highscore))
