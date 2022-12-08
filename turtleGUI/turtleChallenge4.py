import turtle as trt
import random


timmy = trt.Turtle()
trt.colormode(255)
timmy.pensize(5)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 250)
    return r, g, b


directions = [0, 90, 180, 270]

for _ in range(50):
    timmy.color(random_color())
    timmy.setheading(random.choice(directions))
    timmy.forward(10)

screen = trt.Screen()
screen.exitonclick()
