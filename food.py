import turtle
from turtle import Turtle
import random

# set color mode to RGB
turtle.colormode(255)

COLOR_LIST = [
    (26, 109, 164), (194, 38, 81), (237, 161, 50),
    (234, 215, 86), (227, 237, 229), (222, 137, 176), (143, 109, 57), (101, 197, 219), (206, 166, 29),
    (21, 58, 132), (212, 75, 91), (238, 89, 49), (141, 208, 227), (119, 192, 141), (6, 160, 87), (4, 186, 179),
    (106, 108, 198)
]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLOR_LIST))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLOR_LIST))
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
