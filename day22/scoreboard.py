from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 40, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,250)
        self.color('white')
        self.hideturtle()
        self.pl1_score = 0
        self.pl2_score = 0
        self.write(f"{self.pl1_score} : {self.pl2_score}", align=ALIGNMENT, font=FONT)

    def update_pl1_score(self):
        self.pl1_score = self.pl1_score+1
        self.clear()
        self.write(f"{self.pl1_score} : {self.pl2_score}", align=ALIGNMENT, font=FONT)

    def update_pl2_score(self):
        self.pl2_score = self.pl2_score+1
        self.clear()
        self.write(f"{self.pl1_score} : {self.pl2_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=('Courier', 50, 'bold'))

    # def score_count(self):
    #     self.score += 1
    #     self.clear()
    #     self.update_score()
