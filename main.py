import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
window = Screen()
window.setup(600,600)
window.bgcolor("black")
window.title("snake game")
window.tracer(0)

my_snake = Snake()
food = Food()
game_on = True
while game_on:
   my_snake.move()
   window.update()
   time.sleep(0.1)
   window.listen()
   window.onkey(my_snake.up,"o")
   window.onkey(my_snake.down,"l")
   window.onkey(my_snake.right,"m")
   window.onkey(my_snake.left,"k")
   if my_snake.head.distance(food) <= 20:
      food.random_appear()
      my_snake.grow()

   
window.exitonclick()