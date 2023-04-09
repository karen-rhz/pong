from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_paces = 10
        self.y_paces = 10

    def movement(self):
        new_x = self.xcor() + self.x_paces
        new_y = self.ycor() + self.y_paces
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_paces *= -1

    def bounce_x(self):
        self.x_paces *= -1