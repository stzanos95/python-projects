from turtle import Turtle
from constants import *
import random


class CarGenerator:

    def __init__(self):
        self.car_list = []
        self.car_speed = CAR_MOVEMENT

    def generate_car(self, difficulty, max_difficulty):
        generation_chance = random.randint(difficulty, max_difficulty)
        if generation_chance == difficulty:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=CAR_WIDTH, stretch_len=CAR_LENGTH)
            new_car.penup()
            new_car.color(random.choice(CAR_COLORS))
            new_car.goto(SCREEN_SIZE_X / 2,
                         random.randint(-SCREEN_SIZE_Y / 2 + OFFSET_START, SCREEN_SIZE_Y / 2 - OFFSET_FINISH))
            new_car.left(180)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.car_speed)
