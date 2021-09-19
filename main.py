# Lets write the pong game
from turtle import Screen, Turtle
import time
from paddle import Paddle

XPOS1 = -450
XPOS2 = 450



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



paddle1 = Paddle(XPOS1)

paddle2 = Paddle(XPOS2)

#paddle1.build_paddle()


#screen.listen()
#screen.onkey(key="Up", fun=snake.up)
#screen.onkey(key="Down", fun=snake.down)
#screen.onkey(key="Left", fun=snake.left)
#screen.onkey(key="Right", fun=snake.right)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    




screen.exitonclick()

