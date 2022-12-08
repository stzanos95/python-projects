import turtle as trt
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = trt.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("PYTHON")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
playing = True
while playing:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Eating food
    if snake.head.distance(food) < 15:
        food.move()
        snake.grow()
        scoreboard.increase_score()

    # Check collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.game_over()
        snake.reset()
        time.sleep(2)
        scoreboard.reset_score()

    # Check collision with tail
    for tail_part in snake.snake_body[1:]:
        if snake.head.distance(tail_part) < 1:
            scoreboard.game_over()
            snake.reset()
            time.sleep(2)
            scoreboard.reset_score()
    scoreboard.increase_highscore()

scoreboard.game_over()
screen.exitonclick()
