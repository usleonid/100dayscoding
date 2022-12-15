from turtle import Turtle, Screen
import turtle as t
import random

tin = Turtle()
screen = Screen()
tin.shape("classic")
# tinny_the_turtle.color("red")
# for _ in range(4):
#     tin.forward(100)
#     tin.right(90)

# tin = Turtle()
# tom = Turtle()
# terry = Turtle()

# tin.pensize(10)
# for _ in range(15):
#     tin.forward(10)
#     tin.penup()
#     tin.forward(10)
#     tin.pendown()

# def draw_shapes(num_of_sides):
#     for _ in range(num_of_sides):
#         angle = 360/num_of_sides
#         tin.forward(100)
#         tin.right(angle)

# colors = ["red", "green", "blue", "violet", "black", "brown", "orange"]

# for num_of_sides in range(3,11):
#     tin.pencolor(random.choice(colors))
#     draw_shapes(num_of_sides)

# count = 0
# tin.pensize(10)
tin.speed(12)
direction = [0, 90, 180, 270]
t.colormode(255)

def choose_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

angle = 0

while angle < 360:
    tin.pencolor(choose_color())
    tin.seth(angle)
    tin.circle(80)
    angle += 5


# for _ in range(200):
#     tin.pencolor(choose_color())
#     tin.forward(30)
#     tin.setheading(random.choice(direction))
# while count <51:
#     count += 1
#     tin.pencolor(random.choice(colors))
#     # if (-100 < tin.xcor() <100) and (-100 < tin.ycor() <100):
#     # tin.right(random.choice([0,90,180]))
#     distance = random.randint(30,100)
#     direction = [tin.forward(distance), tin.right(90), tin.left(90), tin.back(distance)]
#     random.choice(direction)
    # tin.forward(distance)
    # else:
    #     tin.right(180)
    #     tin.forward(distance)




screen.exitonclick()
