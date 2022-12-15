import turtle as t

tin = t.Turtle()
screen = t.Screen()

def move_forward():
    tin.forward(10)

def move_backward():
    tin.backward(10)

def turn_clockwise():
    tin.right(10)

def turn_counter_clockwise():
    tin.left(10)

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_clockwise, 'd')
screen.onkey(turn_counter_clockwise, 'a')
screen.onkey(screen.resetscreen, 'c')


screen.exitonclick()