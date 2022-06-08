from turtle import Turtle
ALIGMNENT = "center"
FONT = ("Courier", 25, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGMNENT, font=FONT,)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()

