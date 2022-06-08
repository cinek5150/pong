from turtle import Turtle

RIGHT_STARTING_POSITIONS = (380, 0)
LEFT_STARTING_POSITIONS = (-380, 0)
RIGHT_AXIS = 380
LEFT_AXIS = -380
MOVE_DISTANCE = 80


class Racket:

    def __init__(self):
        self.left_racket()
        self.right_racket()

    def spawn(self, position):
        body = Turtle()
        # body.speed('slowest')
        body.penup()
        body.color('white')
        body.shapesize(5,1)
        body.shape('square')
        body.goto(position)
        return body

    def right_racket(self):
        self.right_body = self.spawn(RIGHT_STARTING_POSITIONS)

    def left_racket(self):
        self.left_body = self.spawn(LEFT_STARTING_POSITIONS)

    def right_move_up(self):
        new_y = self.right_body.ycor() + MOVE_DISTANCE
        self.right_body.goto(RIGHT_AXIS, new_y)

    def left_move_up(self):
        new_y = self.left_body.ycor() + MOVE_DISTANCE
        self.left_body.goto(LEFT_AXIS, new_y)

    def right_move_down(self):
        new_y = self.right_body.ycor() - MOVE_DISTANCE
        self.right_body.goto(RIGHT_AXIS, new_y)

    def left_move_down(self):
        new_y = self.left_body.ycor() - MOVE_DISTANCE
        self.left_body.goto(LEFT_AXIS, new_y)
