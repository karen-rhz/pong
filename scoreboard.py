from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.update()

    def update(self):
        # Erases previous score before displaying the new value
        self.clear()
        self.goto(-100, 220)
        self.write(arg=self.player1_score, align="center", font=("Arial", 40, "bold"))
        self.goto(100, 220)
        self.write(arg=f"{self.player2_score}", align="center", font=("Arial", 40, "bold"))

    def player1_scores(self):
        self.player1_score += 1
        self.update()

    def player2_scores(self):
        self.player2_score += 1
        self.update()
