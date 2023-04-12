from turtle import *
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
racers=[]
colour=["red", "yellow", "blue", "green", "black"]
pos=[-120, -90, -60, -30, 0]
race_on = False
for tur in range(0,5):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colour[tur])
    tim.goto(-240, pos[tur])
    racers.append(tim)
user_choice = screen.textinput(title="choose a winner", prompt="Which Turtle will win the race? ")

if user_choice:
    race_on= True

while race_on is True:
    for tur in racers:
        if tur.xcor() > 220:
            winning_col= tur.pencolor()
            print(winning_col)
            if user_choice == winning_col:
                print("You have won the race: ")
            else:
                print("You have lost the race: ")
            race_on = False
        dis = randint(0, 10)
        tur.forward(dis)


screen.exitonclick()

