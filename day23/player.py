import turtle as t

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('black')
        self.speed('fastest')
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        if self.ycor() < 280:
            self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)