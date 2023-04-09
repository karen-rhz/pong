from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):

    def __init__(self, x_cor_paddle, y_cor_paddle):
        """Returns a paddle that will go to a given coordinates."""
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(1, 3)
        self.seth(270)
        self.goto(x_cor_paddle, y_cor_paddle)

    def move_up(self):
        new_y_cor = self.ycor() + 20
        if new_y_cor < 280:
            return self.goto(self.xcor(), new_y_cor)

    def move_down(self):
        new_y_cor = self.ycor() - 20
        if new_y_cor > -280:
            return self.goto(self.xcor(), new_y_cor)