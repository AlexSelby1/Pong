from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color("white")
        
    def move(self):
        new_x = self.ycor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x,new_y)