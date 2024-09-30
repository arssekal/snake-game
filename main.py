import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Showscore
from decoration import Decorate
window = Screen()
window.setup(600,600)
window.bgcolor("black")
window.title("snake game")
window.tracer(0)

decore = Decorate()
my_snake = Snake()
food = Food()
score = Showscore()
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
      score.increase_score()
      food.random_appear()
      my_snake.grow()
   if my_snake.head.xcor() > 250 or my_snake.head.xcor() < -250 or my_snake.head.ycor() > 250 or my_snake.head.ycor() < -250 :
      game_on = False
      score.game_over()
   
window.exitonclick()