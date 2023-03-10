import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake(x=0, y=0, shape='square', color='white')
food = Food()

def ask_to_quite():
    scoreboard.want_to_quite()
    time.sleep(3)
    screen.onkey(gameover, "y")
    screen.onkey(gamecontinue, "n")

def gameover():
    global game_is_on
    game_is_on = False
    scoreboard.game_over()

def gamecontinue():
    time.sleep(0.1)
    scoreboard.clear()
    scoreboard.goto(0,283)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(ask_to_quite, "q")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.score_count()

    # detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        scoreboard.reset_counter()
        snake.reset_snake(x=0, y=0, shape='square', color='white')

    # detect collision with itself
    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            # game_is_on = False
            scoreboard.reset_counter()
            snake.reset_snake(x=0, y=0, shape='square', color='white')

screen.exitonclick()