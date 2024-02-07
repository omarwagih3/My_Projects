import tkinter as tk
from tkinter import font as tkFont
import random

#d13913 red
#59b3df blue
def my_first_check_version():
    #check one row 1
    x_count = 0
    o_count = 0
    for button in buttons_backup[:3]:
        if button["text"] == "X":
            x_count += 1
        elif button["text"] == "O":
            o_count += 1
    if x_count == 3:
        game_result_label.config(text="You Won ^_^")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#59b3df")
    if o_count == 3:
        game_result_label.config(text="You Lose :( ")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#d13913")
    #check two row 2
    x_count = 0
    o_count = 0
    for button in buttons_backup[3:6]:
        if button["text"] == "X":
            x_count += 1
        elif button["text"] == "O":
            o_count += 1
    if x_count == 3:
        game_result_label.config(text="You Won ^_^")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#59b3df")
    if o_count == 3:
        game_result_label.config(text="You Lose :( ")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#d13913")
    #check three row 3
    x_count = 0
    o_count = 0
    for button in buttons_backup[6:]:
        if button["text"] == "X":
            x_count += 1
        elif button["text"] == "O":
            o_count += 1
    if x_count == 3:
        game_result_label.config(text="You Won ^_^")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#59b3df")
    if o_count == 3:
        game_result_label.config(text="You Lose :( ")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#d13913")
    #check four column 1
    x_count = 0
    o_count = 0
    for button in buttons_backup[::3]:
        if button["text"] == "X":
            x_count += 1
        elif button["text"] == "O":
            o_count += 1
    if x_count == 3:
        game_result_label.config(text="You Won ^_^")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#59b3df")
    if o_count == 3:
        game_result_label.config(text="You Lose :( ")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#d13913")
    #check four column 2
    x_count = 0
    o_count = 0
    for button in buttons_backup[1::3]:
        if button["text"] == "X":
            x_count += 1
        elif button["text"] == "O":
            o_count += 1
    if x_count == 3:
        game_result_label.config(text="You Won ^_^")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#59b3df")
    if o_count == 3:
        game_result_label.config(text="You Lose :( ")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#d13913")
    #check four column 3
    x_count = 0
    o_count = 0
    for button in buttons_backup[2::3]:
        if button["text"] == "X":
            x_count += 1
        elif button["text"] == "O":
            o_count += 1
    if x_count == 3:
        game_result_label.config(text="You Won ^_^")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#59b3df")
    if o_count == 3:
        game_result_label.config(text="You Lose :( ")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#d13913")
    #check four diam 1
    x_count = 0
    o_count = 0
    for button in buttons_backup[::4]:
        if button["text"] == "X":
            x_count += 1
        elif button["text"] == "O":
            o_count += 1
    if x_count == 3:
        game_result_label.config(text="You Won ^_^")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#59b3df")
    if o_count == 3:
        game_result_label.config(text="You Lose :( ")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#d13913")
    #check four diam 2
    x_count = 0
    o_count = 0
    for button in buttons_backup[2:7:2]:
        if button["text"] == "X":
            x_count += 1
        elif button["text"] == "O":
            o_count += 1
    if x_count == 3:
        game_result_label.config(text="You Won ^_^")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#59b3df")
    if o_count == 3:
        game_result_label.config(text="You Lose :( ")
        for button in buttons_backup:
            button.config(text = "" ,bg = "#d13913")
    #check Tie
    count = 0
    for button in buttons_backup:
        if button["text"] == "X" or button["text"] == "O":
            count += 1
    if count == 9:
        game_result_label.config(text="Tie No one Win! ")

def check_win_lose_tie():
    # Define the winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    # Check for a win
    for combo in winning_combinations:
        symbols = [buttons_backup[i]["text"] for i in combo]
        if symbols == ["X", "X", "X"]:
            game_result_label.config(text="You Won ^_^" ,fg = "#0c9af9")
            for button in buttons_backup:
                button.config(bg="#59b3df")
            return 1
        elif symbols == ["O", "O", "O"]:
            game_result_label.config(text="You Lose :( " ,fg = "#eb0606")
            for button in buttons_backup:
                button.config(bg="#d13913")
            return 0

    # Check for a tie
    if all(button["text"] in ["X", "O"] for button in buttons_backup):
        game_result_label.config(text="Tie No one Win !!" ,fg = "#1be423")
        for button in buttons_backup:
                button.config(bg="#6c1ee3")

def score_updating():
    global no_x_win
    global no_o_win
    #updating score
    flag = check_win_lose_tie()
    if flag == 1:
        no_x_win += 1
        you_label.config(text =f"You : {no_x_win}")
    elif flag == 0:
        no_o_win += 1
        computer_label.config(text =f"Computer : {no_o_win}")

def click_btn_1():
    #Changing appearance of clicked button
    btn_1.config(text = "X" ,fg = "black" ,bg = "#59b3df")
    buttons.remove(btn_1)

    #Update buttons_backup to reflect the current state
    buttons_backup[0]["text"] = "X"

    #Call the win and tie checking function
    check_win_lose_tie()

    #computer choosing      #We can make it a function and call it within each 
    if buttons:                 # Check that the list in not empty
        random_btn = random.choice(buttons)
        random_btn.config(text = "O" ,fg = "white" ,bg = "#d13913")
        buttons.remove(random_btn)

        #Update buttons_backup to reflect the current state
        index = buttons_backup.index(random_btn)
        buttons_backup[index]["text"] = "O"

        #Call the win and tie checking function
        check_win_lose_tie()

        #update score
        score_updating()
def click_btn_2():
    #Changing appearance of clicked button
    btn_2.config(text = "X" ,fg = "black" ,bg = "#59b3df")
    buttons.remove(btn_2)

    #Update buttons_backup to reflect the current state
    buttons_backup[1]["text"] = "X"

    #Call the win and tie checking function
    check_win_lose_tie()

    #computer choosing
    if buttons:                 # Check that the list in not empty
        random_btn = random.choice(buttons)
        random_btn.config(text = "O" ,fg = "white" ,bg = "#d13913")
        buttons.remove(random_btn)

        #Update buttons_backup to reflect the current state
        index = buttons_backup.index(random_btn)
        buttons_backup[index]["text"] = "O"

        #Call the win and tie checking function
        check_win_lose_tie()

        #update score
        score_updating()
def click_btn_3():
    #Changing appearance of clicked button
    btn_3.config(text = "X" ,fg = "black" ,bg = "#59b3df")
    buttons.remove(btn_3)

    #Update buttons_backup to reflect the current state
    buttons_backup[2]["text"] = "X"

    #Call the win and tie checking function
    check_win_lose_tie()

    #computer choosing
    if buttons:                 # Check that the list in not empty
        random_btn = random.choice(buttons)
        random_btn.config(text = "O" ,fg = "white" ,bg = "#d13913")
        buttons.remove(random_btn)

        #Update buttons_backup to reflect the current state
        index = buttons_backup.index(random_btn)
        buttons_backup[index]["text"] = "O"

        #Call the win and tie checking function
        check_win_lose_tie()

        #update score
        score_updating()
def click_btn_4():
    #Changing appearance of clicked button
    btn_4.config(text = "X" ,fg = "black" ,bg = "#59b3df")
    buttons.remove(btn_4)

    #Update buttons_backup to reflect the current state
    buttons_backup[3]["text"] = "X"

    # Call the win and tie checking function
    check_win_lose_tie()

    #computer choosing
    if buttons:                 # Check that the list in not empty
        random_btn = random.choice(buttons)
        random_btn.config(text = "O" ,fg = "white" ,bg = "#d13913")
        buttons.remove(random_btn)

        #Update buttons_backup to reflect the current state
        index = buttons_backup.index(random_btn)
        buttons_backup[index]["text"] = "O"

        #Call the win and tie checking function
        check_win_lose_tie()

        #update score
        score_updating()
def click_btn_5():
    #Changing appearance of clicked button
    btn_5.config(text = "X" ,fg = "black" ,bg = "#59b3df")
    buttons.remove(btn_5)

    #Update buttons_backup to reflect the current state
    buttons_backup[4]["text"] = "X"

    # Call the win and tie checking function
    check_win_lose_tie()

    #computer choosing
    if buttons:                 # Check that the list in not empty
        random_btn = random.choice(buttons)
        random_btn.config(text = "O" ,fg = "white" ,bg = "#d13913")
        buttons.remove(random_btn)

        #Update buttons_backup to reflect the current state
        index = buttons_backup.index(random_btn)
        buttons_backup[index]["text"] = "O"

        #Call the win and tie checking function
        check_win_lose_tie()

        #update score
        score_updating()
def click_btn_6():
    #Changing appearance of clicked button
    btn_6.config(text = "X" ,fg = "black" ,bg = "#59b3df")
    buttons.remove(btn_6)

    #Update buttons_backup to reflect the current state
    buttons_backup[5]["text"] = "X"

    # Call the win and tie checking function
    check_win_lose_tie()

    #computer choosing
    if buttons:                 # Check that the list in not empty
        random_btn = random.choice(buttons)
        random_btn.config(text = "O" ,fg = "white" ,bg = "#d13913")
        buttons.remove(random_btn)

        #Update buttons_backup to reflect the current state
        index = buttons_backup.index(random_btn)
        buttons_backup[index]["text"] = "O"

        #Call the win and tie checking function
        check_win_lose_tie()

        #update score
        score_updating()
def click_btn_7():
    #Changing appearance of clicked button
    btn_7.config(text = "X" ,fg = "black" ,bg = "#59b3df")
    buttons.remove(btn_7)

    #Update buttons_backup to reflect the current state
    buttons_backup[6]["text"] = "X"

    # Call the win and tie checking function
    check_win_lose_tie()

    #computer choosing
    if buttons:                 # Check that the list in not empty
        random_btn = random.choice(buttons)
        random_btn.config(text = "O" ,fg = "white" ,bg = "#d13913")
        buttons.remove(random_btn)

        #Update buttons_backup to reflect the current state
        index = buttons_backup.index(random_btn)
        buttons_backup[index]["text"] = "O"

        #Call the win and tie checking function
        check_win_lose_tie()

        #update score
        score_updating()
def click_btn_8():
    #Changing appearance of clicked button
    btn_8.config(text = "X" ,fg = "black" ,bg = "#59b3df")
    buttons.remove(btn_8)

    #Update buttons_backup to reflect the current state
    buttons_backup[7]["text"] = "X"

    # Call the win and tie checking function
    check_win_lose_tie()

    #computer choosing
    if buttons:                 # Check that the list in not empty
        random_btn = random.choice(buttons)
        random_btn.config(text = "O" ,fg = "white" ,bg = "#d13913")
        buttons.remove(random_btn)

        #Update buttons_backup to reflect the current state
        index = buttons_backup.index(random_btn)
        buttons_backup[index]["text"] = "O"

        #Call the win and tie checking function
        check_win_lose_tie()

        #update score
        score_updating()
def click_btn_9():
    #Changing appearance of clicked button
    btn_9.config(text = "X" ,fg = "black" ,bg = "#59b3df")
    buttons.remove(btn_9)

    #Update buttons_backup to reflect the current state
    buttons_backup[8]["text"] = "X"

    # Call the win and tie checking function
    check_win_lose_tie()

    #computer choosing
    if buttons:                 # Check that the list in not empty
        random_btn = random.choice(buttons)
        random_btn.config(text = "O" ,fg = "white" ,bg = "#d13913")
        buttons.remove(random_btn)

        #Update buttons_backup to reflect the current state
        index = buttons_backup.index(random_btn)
        buttons_backup[index]["text"] = "O"

        #Call the win and tie checking function
        check_win_lose_tie()

        #update score
        score_updating()

def click_restart():
    #reset all buttons
    for button in buttons_backup:
        button.config(text = "" ,bg = "#353535")

    #backup buttons list to start over again
    for button in buttons_backup:
        buttons.append(button)

    #wipe state label
    game_result_label.config(text = "")


window = tk.Tk()

window.title(f"Tic Tac Toe ^_^")
window.configure(bg = "#1b1b1b")

#Creating buttons and labels for the game
no_x_win = 0
no_o_win = 0
you_label = tk.Label(window ,text= f"You : {no_x_win}" ,font = ("italic",12) ,bg= "#353535" ,fg = "#999999" ,height = 2 ,width = 10)
computer_label = tk.Label(window ,text= f"Computer : {no_o_win}" ,font = ("italic",12) ,bg= "#353535" ,fg = "#999999" ,height = 2 ,width = 10)
game_result_label = tk.Label(window ,text= "" ,font = ("italic",25),bg= "#1b1b1b" ,fg = "#999999" ,width= 10 ,height= 4)
restart_btn = tk.Button(window ,text= "Restart" ,font = ("italic",20) ,fg = "#999999" ,bg = "#353535" ,width = "13" ,height = "1" ,command = click_restart)

#creating 3x3 btns grid for the game
btn_1 = tk.Button(window ,font = ("Bold" ,20) ,fg = "#999999" ,bg = "#353535" ,width = "16" ,height = "5" ,command = click_btn_1)
btn_2 = tk.Button(window ,font = ("Bold" ,20) ,fg = "#999999" ,bg = "#353535" ,width = "16" ,height = "5" ,command = click_btn_2)
btn_3 = tk.Button(window ,font = ("Bold" ,20) ,fg = "#999999" ,bg = "#353535" ,width = "16" ,height = "5" ,command = click_btn_3)
btn_4 = tk.Button(window ,font = ("Bold" ,20) ,fg = "#999999" ,bg = "#353535" ,width = "16" ,height = "5" ,command = click_btn_4)
btn_5 = tk.Button(window ,font = ("Bold" ,20) ,fg = "#999999" ,bg = "#353535" ,width = "16" ,height = "5" ,command = click_btn_5)
btn_6 = tk.Button(window ,font = ("Bold" ,20) ,fg = "#999999" ,bg = "#353535" ,width = "16" ,height = "5" ,command = click_btn_6)
btn_7 = tk.Button(window ,font = ("Bold" ,20) ,fg = "#999999" ,bg = "#353535" ,width = "16" ,height = "5" ,command = click_btn_7)
btn_8 = tk.Button(window ,font = ("Bold" ,20) ,fg = "#999999" ,bg = "#353535" ,width = "16" ,height = "5" ,command = click_btn_8)
btn_9 = tk.Button(window ,font = ("Bold" ,20), fg = "#999999" ,bg = "#353535" ,width = "16" ,height = "5" ,command = click_btn_9)

#making list of the grid to be easy be iterated
buttons = [btn_1 ,btn_2 ,btn_3 ,btn_4 ,btn_5 ,btn_6 ,btn_7 ,btn_8 ,btn_9]
buttons_backup = buttons.copy()

#Positioning
you_label.grid(row = 0,column = 0 ,padx= 50 ,pady = 10)
computer_label.grid(row = 0,column = 2 ,padx= 50 ,pady = 10)
game_result_label.grid(row = 1 ,column = 1,sticky = "nsew")
restart_btn.grid(row = 2,column = 1 ,padx = 2 ,sticky= "ns")
btn_1.grid(row = 3 ,column = 0)
btn_2.grid(row = 3 ,column = 1)
btn_3.grid(row = 3 ,column = 2)
btn_4.grid(row = 4 ,column = 0)
btn_5.grid(row = 4 ,column = 1)
btn_6.grid(row = 4 ,column = 2)
btn_7.grid(row = 5 ,column = 0)
btn_8.grid(row = 5 ,column = 1)
btn_9.grid(row = 5 ,column = 2)


window.mainloop()