from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,283)
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER! Your final score: {self.score}", align=ALIGNMENT, font=('Courier', 24, 'bold'))

    def score_count(self):
        self.score += 1
        self.clear()
        self.update_score()
