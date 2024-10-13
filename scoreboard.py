from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)

    def writeScore(self,score):
        self.clear()
        self.write(f"Score: {score}", align="center", font=("Arial",12,"normal"))
