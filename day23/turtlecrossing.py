import turtle as t
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing game")
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(speed)

    carManager.createCar()
    carManager.moveCar()

    if player.ycor() >= 270:
        if speed > 0.01:
            speed -= 0.01
            scoreboard.level_up()
        player.refresh()

    for car in carManager.carManager:
        if player.distance(car) <= 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()