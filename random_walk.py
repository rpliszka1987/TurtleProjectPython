from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(15)
tim.speed("fastest")
screen = Screen()
colors = ["red", "orange", "blue", "yellow", "cyan", "magenta", "black"]
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))



screen.exitonclick()