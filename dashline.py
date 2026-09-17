from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.bgcolor("green")

tim.shape("turtle")
tim.color("blue1")

for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



screen.exitonclick()