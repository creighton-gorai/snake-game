from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.body = 3
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for part in STARTING_POSITIONS:
            self.add_part(part)

    def add_part(self, position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake.append(snake_part)

    def extend(self):
        self.add_part(self.snake[-1].position())

    def reset(self):
        for part in self.snake:
            part.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part - 1].xcor()
            new_y = self.snake[part - 1].ycor()
            self.snake[part].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
