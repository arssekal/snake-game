from turtle import Turtle
class Showscore(Turtle):
    def __init__(self):
        super().__init__()
        self.scoor = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-260,270)
    def update_score(self):
        self.write(f"score : {self.scoor}   high score: {self.high_score}",font=("arial",20,"normal"))
    def increase_score(self):
        self.clear()
        self.scoor += 10
        self.update_score()
    def game_over(self):
        self.clear()
        self.screen.bgcolor("red")
        self.goto(-150,0) 
        if self.scoor > self.high_score:
            self.high_score = self.scoor
        with open("high_score.txt","r") as file:
            exist_score = int(file.readline())
            if self.high_score > exist_score:
                with open("high_score.txt","w") as file:
                    file.write(str(self.high_score))
            else:
                self.high_score = exist_score
        self.write(f"-----------💀 game over 💀-----------\n\nfinal score : {self.scoor}\nhigh score: {self.high_score}",font=("arial",20,"normal"))