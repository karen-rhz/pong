from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("cyan")
        self.hideturtle()
        self.penup()
        self.goto(-400, 300)
        self.pensize(10)
        self.pendown()
        self.forward(800)
        self.right(90)
        self.forward(600)
        self.right(90)
        self.forward(800)
        self.right(90)
        self.forward(600)