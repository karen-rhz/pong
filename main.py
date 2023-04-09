from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.screensize(canvheight=300, canvwidth=800, bg="black")
screen.setup(height=300, width=800)
screen.title("Pong")
screen.tracer(0)
game_over = False

for _ in range(15):
    middle_lane = Turtle("square")
    middle_lane.penup()
    middle_lane.color("white")
    middle_lane.shapesize(0.25, 1)
    middle_lane.seth(270)
    y_cor_lane = (_*50) - 300
    middle_lane.goto(0, y_cor_lane)

player1_paddle = Paddle(-300, 0)

screen.listen()

screen.onkey(player1_paddle.move_up, "w")
screen.onkey(player1_paddle.move_down, "s")

player2_paddle = Paddle(300, 0)
screen.onkey(player2_paddle.move_up, "Up")
screen.onkey(player2_paddle.move_down, "Down")

ball = Ball()
while not game_over:
    time.sleep(0.1)
    screen.update()
    ball.movement()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.ycor() > 270 and ball.distance(player2_paddle) < 50 \
            or ball.ycor() < -270 and ball.distance(player1_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 320 or ball.xcor() < -320:
        print("Game over")
        game_over = True

screen.exitonclick()