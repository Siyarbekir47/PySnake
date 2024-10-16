from turtle import Screen
from Class.scoreboard import Scoreboard
from Class.snake import Snake
from Class.food import Food
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("PySnake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    scoreboard.update_score()
    snake.move()
    time.sleep(0.1)

    #detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        food.refresh()
        snake.extend()
    #detect collision with wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_is_on = False
        scoreboard.game_over()
    #detect collision with tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()