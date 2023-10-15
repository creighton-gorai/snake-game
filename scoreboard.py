from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.saved_score = file.read()
        self.high_score = int(self.saved_score)
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

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False,
                   align="center", font=('Arial', 20, 'normal'))
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
