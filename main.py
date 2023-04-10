from turtle import Screen
from paddle import Paddle
from ball import Ball
from border import Border
import time
from scoreboard import Score

screen = Screen()
screen.screensize(canvheight=600, canvwidth=800, bg="black")
screen.title("Pong")
screen.tracer(0)
game_over = False

player1_paddle = Paddle(-380, 0)

screen.listen()

screen.onkey(player1_paddle.move_up, "w")
screen.onkey(player1_paddle.move_down, "s")

player2_paddle = Paddle(380, 0)
screen.onkey(player2_paddle.move_up, "Up")
screen.onkey(player2_paddle.move_down, "Down")

border = Border()
ball = Ball()
score = Score()
score.update()
while not game_over:
    time.sleep(0.1)
    screen.update()
    ball.movement()
    # Detect collosion with the top and bottom wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect collosion with the player's paddle
    if ball.ycor() > 320 and ball.distance(player2_paddle) < 50 \
            or ball.ycor() < -320 and ball.distance(player1_paddle) < 50:
        ball.bounce_x()

    # Detect collosion with the left and right wall
    # When the player misses to hit the ball
    # If player 1 misses the ball, the point will be given to player 2
    if ball.xcor() < -385:
        score.player2_scores()
        ball.ball_in_middle()

    # If player 2 misses the ball, the point will be given to player 1
    if ball.xcor() > 385:
        score.player1_scores()
        ball.ball_in_middle()


screen.exitonclick()