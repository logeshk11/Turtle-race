from turtle import *
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
racers=[]
colour=["red", "yellow", "blue", "green", "black"]
pos=[-120, -90, -60, -30, 0]
race_on = True
logesh = Turtle(shape='turtle')
logesh.color('orange')
logesh.penup()
logesh.goto(-240, 30)
level = screen.textinput(title="Enter level", prompt="easy, medium or hard")
if level == "easy":
    speed=15
elif level =="medium":
    speed=11
else:
    speed=9
def move_foward():
    logesh.forward(speed)

for tur in range(0,5):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colour[tur])
    tim.goto(-240, pos[tur])
    racers.append(tim)
screen.title("Welcome to race: ")
print("Race Start")

while race_on is True:
    for tur in racers:
        if tur.xcor() > 220:
            print("You lose")
            race_on= False
            break
        elif logesh.xcor() >210:
            print("You win")
            race_on = False
            break
        dis = randint(0, 10)
        tur.forward(dis)
        screen.listen()
        screen.onkey(fun= move_foward, key= "w")



screen.exitonclick()

