from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False,
                   align="center", font=('Arial', 20, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False,
                   align="center", font=('Arial', 20, 'normal'))

    # def game_over (self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, align="center", font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False,
                   align="center", font=('Arial', 20, 'normal'))

