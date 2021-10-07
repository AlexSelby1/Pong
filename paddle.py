from turtle import Turtle

P1_STARTING_POSITIONS = (350, 0)
P2_STARTING_POSITIONS = (-350, 0)

UP = 90
DOWN = 270

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.pu()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        