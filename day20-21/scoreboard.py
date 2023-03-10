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
        with open("data.txt") as file:
            contents = file.read()
            self.high_score = int(contents)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def want_to_quite(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Are you sure want to quite? Type Y or N.", align=ALIGNMENT, font=('Courier', 24, 'bold'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.score))
        self.write(f"GAME OVER!\nYour high score of current session of games: {self.high_score}", align=ALIGNMENT, font=('Courier', 24, 'bold'))

    def reset_counter(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    def score_count(self):
        self.score += 1
        self.clear()
        self.update_score()
