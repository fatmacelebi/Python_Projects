import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()

car = CarManager()


game_is_on = True
car_speed = 0.1
while game_is_on:
    time.sleep(car_speed)
    screen.update()
    car.create_car()
    car.move_left()

    screen.onkey(player.move_turtle, "Up")

    # Player reaches to top
    if player.finish_pos():
        score.increase_score()
        car_speed = car_speed / 2

    # turtle collides with cars
    for cars in car.car_list:
        if cars.distance(player) < 20:
            score.game_over_print()
            game_is_on = False

screen.exitonclick()




