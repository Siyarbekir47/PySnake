
from turtle import Turtle,Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("PySnake")
screen.tracer(0)



snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

# TODO
# detect collision with wall
# detect collision with tail
# detect collision with food
# create a scoreboard



screen.exitonclick()