import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_coordinates = pd.read_csv("50_states.csv")

states_guessed = set()

while len(states_guessed) < 50:

    answer = screen.textinput(title=f"{len(states_guessed)}/50 States Guessed", prompt="What is another State's Name?").upper()

    answer_row = state_coordinates[state_coordinates["state"].str.upper() == answer.upper()]

    if len(answer_row) > 0:
        print(answer_row)
        states_guessed.add(answer_row["state"])

        turtle.penup()
        turtle.goto(x=answer_row["x"], y=answer_row["y"])
        
        turtle.write(answer_row["state"])

screen.exitonclick()





# way to get the coordinates on a turtle screen by clicking
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
