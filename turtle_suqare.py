from turtle import Turtle, Screen
# Turtle drawing a square

tim = Turtle()
tim.shape("turtle")
tim.color("blue1")

for _ in range(4):
    tim.forward(200)
    tim.right(90)

screen = Screen()
screen.exitonclick()