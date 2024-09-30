from turtle import Turtle
class Decorate(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("green")
        self.pensize(2)
        self.penup()
        self.goto(270,270)
        self.left(90)
        for _ in range(4):
            self.left(90)
            self.pendown()
            self.forward(540)