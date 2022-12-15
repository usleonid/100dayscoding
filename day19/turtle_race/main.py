import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
x = -230
y = -125
turtles = []
is_race_on = False

for i in range(6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 50
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is winner!")
            else:
                print(f"You lose!The {win_color} turtle is winner. ")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()