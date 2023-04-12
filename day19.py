from turtle import Turtle
from turtle import Screen

tim = Turtle()
screen = Screen()

tim.forward(5)
def forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="w", fun=forward)

screen.exitonclick()
