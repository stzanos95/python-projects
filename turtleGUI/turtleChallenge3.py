from turtle import Turtle, Screen
import random


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SeaGreen"]
timmy = Turtle()
timmy.penup()
timmy.setx(-50)
timmy.sety(300)
timmy.pendown()


def draw_shape(sides):
    timmy.pencolor(random.choice(colors))
    for _ in range(sides):
        angle = 360 / sides
        timmy.forward(100)
        timmy.right(angle)


for sides in range(3, 50):
    draw_shape(sides)

screen = Screen()
screen.exitonclick()
