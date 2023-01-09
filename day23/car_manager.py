import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.carManager = []

    def createCar(self):
        random_int = random.randint(1,7)
        if random_int == 1:
            car = t.Turtle('square')
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            car.setheading(180)
            self.carManager.append(car)

    def moveCar(self):
        for car in self.carManager:
            car.forward(STARTING_MOVE_DISTANCE)

