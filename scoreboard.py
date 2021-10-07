from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.pu()
        self.color("white")
        self.goto(0, 200)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.write(f"{self.p1_score}       {self.p2_score}", align="center", font=('Barcade', 70, 'bold'))
        
        
    def p1_increase_score(self):
        self.p1_score +=1
        self.clear()
        self.update_scoreboard()
        
    def p2_increase_score(self):
        self.p2_score +=1
        self.clear()
        self.update_scoreboard()