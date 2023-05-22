from turtle import Turtle
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.xcordinate = 0
        self.create_body()
        self.head =self.segments[0]
    def create_body(self):
        for position in range(3):
            if position == 0:
                new_segment = Turtle(shape="circle")
            else:
                new_segment = Turtle(shape="square")

            new_segment.penup()
            new_segment.color("white")

            new_segment.setx(self.xcordinate)
            self.segments.append(new_segment)
            self.xcordinate -= 20
    def movesnake(self):
        # for segment in segments:
        #     segment.forward(10)
        # move segements without cutting when direction change
        for segment_number in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[segment_number - 1].xcor()  # move to lowersegment
            newy = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # self.movesnake()
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # self.movesnake()
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # self.movesnake()
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # self.movesnake()