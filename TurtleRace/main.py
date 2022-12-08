import turtle as trt
import random


def random_sprint(turtle):
    turtle.forward(random.randint(1, 20))
    return turtle.xcor()


def screen_message(msg):
    messenger = trt.Turtle()
    messenger.color("White")
    messenger.color("Black")
    messenger.write(msg)
    messenger.color("White")


max_width = 1500
max_height = 250
delta_h = 50
screen = trt.Screen()
screen.setup(width=max_width, height=max_height)
selected_color = screen.textinput(title="Betting begins!", prompt="Which turtle will win the race? ")

turtle_colors = ["Red", "Green", "Yellow", "Blue", "Purple"]
ycoord = [-100, -50, 0, 50, 100]
turtles = []

for i in range(len(turtle_colors)):
    turtle = trt.Turtle(shape="turtle")
    turtle.speed(2)
    turtle.penup()
    turtle.color(turtle_colors[i])
    turtle.goto(x=-max_width/2+20, y=ycoord[i])
    turtles.append(turtle)

finished = False
while not finished:
    for i, color in enumerate(turtle_colors):
        x = random_sprint(turtles[i])
        if x > max_width / 2:
            finished = True
            screen_message("Winner is the {} turtle!".format(color))
            winner = color
            break

if selected_color.capitalize() == winner.capitalize():
    print("You won the bet!")
else:
    print("You lost the bet...")
screen.exitonclick()
