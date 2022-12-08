import turtle as trt
import random


timmy = trt.Turtle()
trt.colormode(255)
timmy.speed("fast")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 250)
    return r, g, b


rotation = 10
for _ in range(round(360/rotation)):
    timmy.pencolor(random_color())
    timmy.circle(200)
    timmy.right(rotation)

screen = trt.Screen()
screen.exitonclick()
