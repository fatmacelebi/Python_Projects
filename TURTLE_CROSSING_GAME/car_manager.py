from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_list = []

    def create_car(self):
        rand_change = random.randint(1, 6)
        if rand_change == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1, outline=1)
            rand_y = random.randint(-250, 250)
            new_car.goto(350, rand_y)
            self.car_list.append(new_car)

    def move_left(self):
        for cars in self.car_list:
            cars.backward(STARTING_MOVE_DISTANCE)




