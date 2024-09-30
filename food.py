from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.8)
        self.color("yellow")
        self.penup()
        self.random_appear()
    def random_appear(self):
        x = random.randint(-265,265)
        y = random.randint(-265,265)
        self.goto(x,y)
    
    