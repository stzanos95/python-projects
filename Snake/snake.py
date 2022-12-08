import turtle as trt

POS_DISTANCE = 200
MOVE_DISTANCE = 10 
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(3):
            turtle = trt.Turtle()
            turtle.shape("square")
            turtle.color("White")
            turtle.penup()
            turtle.goto(x=-i*POS_DISTANCE, y=0)
            self.snake_body.append(turtle)

    def move(self):
        for pos in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[pos - 1].xcor()
            new_y = self.snake_body[pos - 1].ycor()
            self.snake_body[pos].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        turtle = trt.Turtle()
        turtle.shape("square")
        turtle.color("White")
        turtle.penup()
        turtle.goto(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())
        self.snake_body.append(turtle)

    def reset(self):
        for piece in self.snake_body:
            piece.goto(10000000, 10000000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
