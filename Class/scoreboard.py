from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial",12,"normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"You lost! your socre is: {self.score}",align="center",font=("Arial",20,"normal"))