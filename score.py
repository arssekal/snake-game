from turtle import Turtle
class Showscore(Turtle):
    def __init__(self):
        super().__init__()
        self.scoor = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-260,270)
    def update_score(self):
        self.write(f"score : {self.scoor}",font=("arial",20,"normal"))
    def increase_score(self):
        self.clear()
        self.scoor += 10
        self.update_score()
    def game_over(self):
        self.clear()
        self.screen.bgcolor("red")
        self.goto(-100,0)
        self.write(f"game over\nfinal score : {self.scoor}",font=("arial",20,"normal"))
