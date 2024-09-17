from turtle import Screen, Turtle
import random


is_racing_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="which turtle will win the race")

colors=["red","green","blue","yellow","purple"]
all_tuttles=[]
y_positions=[-70,-40,-10,20,50]
for i in range(len(colors)):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[i])
    all_tuttles.append(new_turtle)
if user_bet:
    is_racing_on=True

while is_racing_on:
    for turtle in all_tuttles:
        if turtle.xcor()>230:
            is_racing_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! the {winning_color} turtle is the winner")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()