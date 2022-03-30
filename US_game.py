import turtle
import pandas as pd
listofguess = []
while len(listofguess)<50:
    screen = turtle.Screen()
    screen.title(f"U.S. Game number")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    state = screen.textinput(title=f"correct states = {len(listofguess)}/50", prompt="What's another state's name? ("
                                                                                     "type exit to terminate)")
    if state == "exit":
        screen.bye()
    states_df =pd.read_csv("50_states.csv")
    mouse = turtle.Turtle()
    print(states_df[states_df.state == state])
    slist = states_df[states_df.state == state].values.tolist()
    if len(slist) == 0:
        pass
    else:
        flist = slist[0]
        the_state = flist[0]
        x = flist[1]
        y = flist[2]
        print(the_state, x ,y)
        mouse.up()
        mouse.setposition(x, y)
        mouse.write(the_state)
        if the_state not in listofguess:
            listofguess.append(the_state)
        else:
            continue
