from turtle import Turtle
class Snake:
    def __init__(self):
        self.positions = [(-40,0),(-20,0),(0,0)]
        self.turtles = []
        self.create_snake()
    def create_snake(self):
        for i in range(len(self.positions)):
            new_turtle = Turtle("square")
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(self.positions[i])
            self.turtles.append(new_turtle)
    def move(self):
        self.head = self.turtles[-1]
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(200)
        self.head.left(90)




