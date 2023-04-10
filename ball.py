from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_paces = 10
        self.y_paces = 10
        self.ball_speed = 0

    def movement(self):
        new_x = self.xcor() + self.x_paces
        new_y = self.ycor() + self.y_paces
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_paces *= -1

    def bounce_x(self):
        self.x_paces *= -1

    def ball_in_middle(self):
        # Increase the ball speed everytime someone scores
        if self.ball_speed <= 10:
            self.ball_speed += 1
            self.speed(self.ball_speed)
        self.goto(0, 0)
        # Make the ball go the other way.
        self.bounce_x()
