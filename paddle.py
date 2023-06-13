from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.create(pos)

    def create(self, pos):
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.setposition(pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def reset_paddle(self, pos):
        self.setposition(pos)
