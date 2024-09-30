from turtle import Turtle
class Snake:
    def __init__(self):
        self.positions = [(-40,0),(-20,0),(0,0)]
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[-1]
        self.head.color("orange")
    def create_snake(self):
        for i in range(len(self.positions)):
            new_turtle = Turtle("square")
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(self.positions[i])
            self.turtles.append(new_turtle)
    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)
    def grow(self):
        new_turtle = Turtle("square")
        new_turtle.color('white')
        new_turtle.penup()
        self.turtles.insert(0,new_turtle)
    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)






