#snake game
import time
from turtle import Turtle,Screen
from snake import  Snake
screen = Screen()


screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")

# does not show turtle
screen.tracer(0)

# create snake body
snake = Snake()

# listen to key stokes
screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)




game_ison = True
# move snake
while game_ison:
    #the loop hold for one second before going on
    time.sleep(1)
    # show snake once complete
    snake.movesnake()

    screen.update()


screen.exitonclick()
