import turtle as t

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(t.Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color('white')
        self.speed('fastest')
        self.goto(x_pos, y_pos)
        self.setheading(UP)

    def move_up(self):
        self.setheading(UP)
        if self.ycor() < 240:
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(DOWN)
        if self.ycor() > -240:
            self.forward(MOVE_DISTANCE)

    # def up(self):
    #     if self.heading() != DOWN:
    #         self.setheading(UP)
    #
    # def down(self):
    #     if self.heading() != UP:
    #         self.setheading(DOWN)