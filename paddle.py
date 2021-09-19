#create a paddle class

from turtle import Turtle



MOVEDISTANCE = 20

#create a paddle
#paddle will be made up of a stretched square

class Paddle:


    def __init__(self, x_pos):
        self.paddle = []
        self.x_pos = x_pos
        self.y_pos = 0
        self.build_paddle()
        

    def build_paddle(self):
        new_paddle = Turtle("square")
        new_paddle.penup()
        new_paddle.color("white")
        new_paddle.shapesize(5, 1, 1)
        new_paddle.goto(self.x_pos, 0)
        
    

    #def build_paddle(self, length):
        #for i in range(length):
            #new_paddle = Turtle("square")
            #new_paddle.penup()
            #new_paddle.color("white")
            #self.paddle.append(new_paddle)
            #if len(self.paddle) == 0:
            #new_paddle.setpos((self.x_pos - (self.paddle.index(new_paddle)*20)), 0)

