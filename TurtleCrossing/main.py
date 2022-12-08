from constants import *
from turtle import Screen, Turtle
from level import Level
from game_turtle import GameTurtle
from car_generator import CarGenerator
import time


def draw_line(y):
    line_turtle = Turtle()
    line_turtle.color("Black")
    line_turtle.penup()
    line_turtle.goto(-SCREEN_SIZE_X / 2, y)
    while line_turtle.xcor() < SCREEN_SIZE_X / 2:
        line_turtle.pendown()
        line_turtle.forward(TURTLE_MOVEMENT)
        line_turtle.penup()
        line_turtle.forward(TURTLE_MOVEMENT)


# Screen setup
screen = Screen()
screen.setup(SCREEN_SIZE_X, SCREEN_SIZE_Y)
screen.title(SCREEN_TITLE)
screen.bgcolor(SCREEN_COLOR)
screen.tracer(0)
screen.listen()

# Lines drawing
draw_line(-SCREEN_SIZE_Y / 2 + OFFSET_START)
draw_line(SCREEN_SIZE_Y / 2 - OFFSET_FINISH)

# Level setup
level = Level()
cars = CarGenerator()

# Turtle setup
game_turtle = GameTurtle()
screen.onkey(game_turtle.move_up, "Up")

# Game start
game_on = True
while game_on:
    cars.generate_car(level.difficulty, level.max_difficulty)
    cars.move_cars()
    screen.update()
    time.sleep(0.02)

    # Detecting collision
    for car in cars.car_list:
        if game_turtle.distance(car.xcor(), car.ycor()) < COLLISION_DB:
            game_on = False
            level.game_over()
    if game_turtle.ycor() >= SCREEN_SIZE_Y / 2 - OFFSET_FINISH:
        level.next()
        cars.car_speed += 1
        game_turtle.reset_pos()

# Background
screen.exitonclick()
