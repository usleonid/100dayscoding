# import colorgram
#
# list_of_colours = []
#
# colours = colorgram.extract('image.jpg', 100)
# # print(colors)
#
# for color in colours:
#     list_of_colours.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(list_of_colours)

import turtle as t
import random

list_of_colours = [(200, 12, 32), (232, 251, 242), (251, 238, 15), (39, 76, 190), (38, 217, 69), (237, 226, 5), (230, 159, 45), (28, 39, 158), (215, 75, 13), (15, 155, 15), (199, 14, 10), (243, 34, 165), (241, 245, 250), (69, 10, 30), (231, 16, 122), (61, 15, 8), (225, 140, 209), (10, 97, 62), (222, 161, 7), (52, 212, 230), (17, 19, 44), (11, 227, 239), (236, 156, 219), (85, 74, 210), (80, 210, 158), (88, 233, 197), (60, 233, 241), (4, 66, 40), (215, 89, 54), (176, 181, 223), (229, 173, 167), (6, 245, 223), (248, 9, 47), (3, 81, 117), (10, 54, 249)]
t.colormode(255)

tin = t.Turtle()
screen = t.Screen()
# screen.screensize(200.0,200.0)
# print(screen.screensize())
tin.penup()
tin.hideturtle()
x = -340.0
y = -340.0
# tin.setposition(x, y)

# tin.pensize(20)
# tin.pendown()
def horizontal_line():
    for _ in range(9):
        # tin.pencolor(random.choice(list_of_colours))
        tin.dot(20, random.choice(list_of_colours))
        tin.forward(50)
    tin.pencolor(random.choice(list_of_colours))
    tin.dot(20)

for _ in range(10):
    tin.setposition(x, y)
    horizontal_line()
    y += 50

screen.exitonclick()