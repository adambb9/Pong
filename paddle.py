#create a paddle class

from turtle import Turtle



MOVEDISTANCE = 20

#create a paddle
#paddle will be made up of a stretched square

class Paddle(Turtle):

    def __init__(self, x_pos):
        self.xpos = x_pos
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1, 1)
        self.color("white")
    
    def move_up(self):
        current_ypos = self.ycor()
        new_ypos = current_ypos + 20
        self.goto(self.xpos, new_ypos)

    def move_down(self):
        current_ypos = self.ycor()
        new_ypos = current_ypos - 20
        self.goto(self.xpos, new_ypos)


    

    
        

        



    
        

    



    
    





        







   

