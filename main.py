
from turtle import Turtle,Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("PySnake")
score = 3
snakeList = []
screen.tracer(0)


snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)




#create snake food
# detect collision with food
# create a scoreboard
# detect collision with wall
# detect collision with tail
# #








screen.exitonclick()