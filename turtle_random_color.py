import turtle as t
import random

tim = t.Turtle()
tim.pensize(15)
t.colormode(255)
tim.speed("fastest")
screen = t.Screen()
directions = [0, 90, 180, 270]

def random_color():
    """Returns a tuple of (r,g,b) colors"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()