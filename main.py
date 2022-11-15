from turtle import Turtle as t, Screen
import random

csaba = t()
colors = ["red","blue","yellow","purple","orange","black","green"]

def draw_shape(num_side):
    angles = 360 / num_side
    for _ in range(num_side):
       csaba.forward(100)
       csaba.right(angles)


for shape_side_n in range(3, 11):
    csaba.color(random.choice(colors))
    draw_shape(shape_side_n)

def draw_shape(num_side):
    angles = 360 / num_side
    for _ in range(num_side):
       csaba.forward(100)
       csaba.left(angles)

for shape_side_n in range(3, 11):
    csaba.color(random.choice(colors))
    draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()