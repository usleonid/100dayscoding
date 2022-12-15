import random
from turtle import Turtle

MOVE_DISTANCE = 20
START_DIRECTION = 45

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('white')
        self.speed('fastest')
        self.goto(0, 0)
        self.cur_dir = START_DIRECTION
        self.setheading(self.cur_dir)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def change_direction(self):
        self.cur_dir = 180 - self.cur_dir
        self.setheading(self.cur_dir)

    def change_angle(self):
        self.cur_dir = -self.cur_dir
        self.setheading(self.cur_dir)

    def refresh(self):
        self.goto(0, 0)
