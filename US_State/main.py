import turtle
from turtle import Turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
all_state = data["state"].to_list()
screen = turtle.Screen()
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

guess_list = []

while len(guess_list) < 50:
    answer = screen.textinput(title=f"{len(guess_list)}/50 Guess the State", prompt="What's other state name?")
    if answer == "exit":
        break
    if answer.lower() in all_state:
        guess_list.append(answer)
        state = data[data.state == answer]
        x_cor = int(state.x)
        y_cor = int(state.y)
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.setposition(x_cor, y_cor)
        new_turtle.write(f"{answer}", align="right")

