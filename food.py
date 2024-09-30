from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.random_appear()
    def random_appear(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)
    
    