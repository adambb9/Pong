from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("red")
        self.speed("fastest")
    
    
    def initialise_ball(self):
        random_heading = random.randint(0, 360)
        self.setheading(random_heading)

    def move_ball(self):
        self.forward(20)

    def ball_bounce(self):
        self.forward(0)
        current_heading = self.heading()
        angle = (180 - current_heading) + 180
        self.setheading(angle)
        self.forward(20)
        



    