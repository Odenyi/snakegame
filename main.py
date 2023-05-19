#snake game
import time
from turtle import Turtle,Screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
xcordinate = 0
screen.tracer(0)
segments =[]
# create snake body
for position in range(3):

    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")


    new_segment.setx(xcordinate)
    segments.append(new_segment)
    xcordinate -= 20
screen.update()
game_ison = True
# move snake
while game_ison:
    time.sleep(0.1)
    # for segment in segments:
    #     segment.forward(10)
    # move segements

    screen.update()


screen.exitonclick()
