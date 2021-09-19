#create a paddle class

from turtle import Turtle



MOVEDISTANCE = 20

#create a paddle
#paddle will be made up of a stretched square

class Paddle(Turtle):

    def __init__(self, x_pos):
        self.xpos = x_pos
        self.ypos = 0
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1, 1)
        self.color("white")
        self.goto(self.xpos, self.ypos)
        
    
    def move_up(self):
        current_ypos = self.ycor()
        self.ypos = current_ypos + 20
        self.goto(self.xpos, self.ypos)

    def move_down(self):
        current_ypos = self.ycor()
        self.ypos = current_ypos - 20
        self.goto(self.xpos, self.ypos)


    

    
        

        



    
        

    



    
    





        







   

