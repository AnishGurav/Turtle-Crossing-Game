from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

import random

class CarManager():
    def __init__(self):

        self.cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(x=280, y=random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for cars in self.cars:
            cars.backward(self.car_speed)

    def next_lvl(self):
        self.car_speed += MOVE_INCREMENT



