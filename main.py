from turtle import Turtle, Screen
from snake import Snake
window = Screen()
window.setup(600,600)
window.bgcolor("black")
window.title("snake game")

my_snake = Snake()
game_on = True
while game_on:
   my_snake.move()

window.exitonclick()