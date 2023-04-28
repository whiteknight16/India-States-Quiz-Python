import pandas as pd
import turtle

data=pd.read_csv("./india_states.csv")

screen=turtle.Screen()
screen.title("India States Game")
screen.bgcolor("Black")
screen.listen()
screen.addshape("./india-state.gif")
turtle.shape("./india-state.gif")
guessed_list=[]
i=0
while(i!=28):
    answer=screen.textinput(f"Guess the state {i}/28","What's another state name? ").title()
    
    if (answer=="Exit"):
        missing_states=[state for state in data["state"].to_list() if state not in guessed_list]
        pd.DataFrame(missing_states).to_csv("states_to_learn.csv") 
        break
    
    state_list=data["state"].to_list()
    if answer in state_list:
        state_index=(state_list.index(answer))

        #Setting Coordinate
        x_pos=data["x"][state_index]
        y_pos=data["y"][state_index]
        pos=(x_pos,y_pos)

        #Setting Turtle
        t=turtle.Turtle()
        t.hideturtle()
        t.pu()
        t.setpos(pos)
        t.pd()
        t.color("orange")
        t.write(answer,font=("Arial",8,"bold"))
        guessed_list.append(answer)
        i+=1


screen.exitonclick()