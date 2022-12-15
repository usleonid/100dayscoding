import turtle as t
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-pong game")
screen.tracer(0)

paddle_right = Paddle(x_pos=350, y_pos=0)
paddle_left = Paddle(x_pos=-350, y_pos=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

game_is_on = True
speed = 0.1
while game_is_on:
    screen.update()
    time.sleep(speed)

    if ball.xcor() < 350 and ball.xcor() > -350:
        if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
            ball.change_direction()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.change_angle()
        ball.move()
    else:
        if ball.xcor() >= 350:
            scoreboard.update_pl1_score()
        elif ball.xcor() <= -350:
            scoreboard.update_pl2_score()
        speed -= 0.005
        ball.change_direction()
        ball.refresh()
    if speed <= 0.005:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()