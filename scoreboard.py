from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier", 77, "normal"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.color("white")
        self.setposition(0, 200)
        self.write(f"{self.l_score}   {self.r_score}", False, ALIGNMENT, FONT)

    def update_score(self):
        self.clear()
        self.print_score()
