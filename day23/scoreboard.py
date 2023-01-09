from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-230,250)
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=('Courier', 24, 'bold'))

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_level()
