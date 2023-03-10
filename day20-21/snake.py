import turtle as t

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, x, y, shape, color):
        self.snake = []
        self.create_snake(shape, color, x, y)
        self.head = self.snake[0]

    def create_snake(self, shape, color, x, y):
        for _ in range(3):
            self.add_snake_part(shape, color, x, y)

    def reset_snake(self, x, y, shape, color):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake(shape, color, x, y)
        self.head = self.snake[0]
        self.create_snake(shape, color, x, y)

    def add_snake_part(self, shape, color, x, y):
        snake_part = t.Turtle(shape)
        snake_part.penup()
        snake_part.color(color)
        snake_part.goto(x, y)
        x -= 20
        self.snake.append(snake_part)

    def extend_snake(self):
        self.add_snake_part(x=self.snake[-1].xcor(), y=self.snake[-1].ycor(), color='white', shape='square')

    def move(self):
        for part_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[part_num-1].xcor()
            new_y = self.snake[part_num-1].ycor()
            self.snake[part_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

