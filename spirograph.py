from turtle import Turtle as t, Screen , colormode
import random

csaba = t()

directions = [0, 90, 180, 270]
csaba.pensize(2)
csaba.speed("fastest")
colors = ["yellow","green","yellow","brown","purple", "red","blue","black"]

for _ in range(35):

    csaba.color(random.choice(colors))
    current_heading = csaba.heading()
    csaba.circle(100)

    csaba.setheading(current_heading + 10)
    csaba.circle(100)



screen = Screen()
screen.exitonclick()