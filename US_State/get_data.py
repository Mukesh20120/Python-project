import pandas as pd

data = pd.read_csv("50_states.csv")
list_state = data["state"]
list_xcor = data["x"]
list_ycor = data["y"]
