from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
for i in range(4):
    timmy.forward(200)
    timmy.right(90)

screen = Screen()
screen.exitonclick()

