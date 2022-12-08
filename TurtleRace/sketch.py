import turtle as trt

turtle = trt.Turtle()
screen = trt.Screen()


def forward():
    turtle.forward(30)


def left():
    turtle.left(90)


def right():
    turtle.right(90)


def back():
    turtle.back(30)


screen.onkey(forward, "Up")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(back, "Down")
screen.listen()
screen.exitonclick()
