# Lets write the pong game
from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball

PLAYER1 = -450
PLAYER2 = 450



screen  = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong 2021")
screen.tracer(0)


border = Turtle()
border.hideturtle()
border.penup()
border.color("white")
border.pensize(5)
border.goto(0, -290)
border.setheading(90)
for i in range(20):
    border.pendown()
    border.forward(15)
    border.penup()
    border.forward(15)



paddle1 = Paddle(PLAYER1)

paddle2 = Paddle(PLAYER2)

ball = Ball()

screen.listen()
screen.onkey(key="w", fun=paddle1.move_up)
screen.onkey(key="s", fun=paddle1.move_down)
screen.onkey(key="Up", fun=paddle2.move_up)
screen.onkey(key="Down", fun=paddle2.move_down)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    
    


screen.exitonclick()

