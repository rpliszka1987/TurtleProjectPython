from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.bgcolor("green")
tim.shape("turtle")
sides = 3
colors = ["red", "orange", "blue", "yellow", "cyan", "magenta", "black"]

while sides < 11:
    tim.color(random.choice(colors))
    for _ in range(sides):
        tim.forward(100)
        tim.right(360/sides)
    sides += 1

screen.exitonclick()