from turtle import Turtle
START_POS = [(0,0),(-20,0),(-40,0)]
MOVE = 20
UP =90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]
    def create_snake(self):
        for pos in START_POS:   
            self.add_segment(pos)
    def add_segment(self,pos):
        new_seg =Turtle("square")
        new_seg.color("medium sea green")
        new_seg.penup()
        new_seg.goto(pos)
        self.seg.append(new_seg)

    def extend(self):
        self.add_segment(self.seg[-1].pos())
    def move(self):
        for seg_n in range(len(self.seg)-1,0,-1):
            new_x = self.seg[seg_n-1].xcor()
            new_y = self.seg[seg_n-1].ycor()
            self.seg[seg_n].goto(new_x,new_y)
        self.head.forward(MOVE)

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
          
