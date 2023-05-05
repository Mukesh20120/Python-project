from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Welcome to the turtle race", prompt="On color which turtle you are going to bet? " )

color = ["yellow", "red", "blue", "orange", "green"]
y_axis = [-100, -50, 0, 50, 100]
all_turtle = []
for i in range(0, 5):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_axis[i])
    all_turtle.append(new_turtle)
start_race = False
if user_bet:
    start_race = True

while start_race:
    for tut in all_turtle:
        if tut.xcor() > 230:
            start_race = False
            if user_bet == tut.pencolor():
                print("You won the bet you get 1000 point for that")
            else:
                print(f"You lose :( try again later winner is {tut.pencolor()}")
        random_no = random.randint(0, 10)
        tut.forward(random_no)

screen.exitonclick()
