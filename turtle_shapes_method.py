from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
sides = 3
colors = ["red", "orange", "blue", "yellow", "cyan", "magenta", "black"]

def draw_shape(num_of_sides):
    tim.color(random.choice(colors))
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    draw_shape(shape_side_n)

screen.exitonclick()