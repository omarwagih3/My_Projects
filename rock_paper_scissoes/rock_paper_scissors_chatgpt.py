import time
import random
#rules of wining
rules ={
    "s" : "p",
    "p" : "r",
    "r" : "s"
}

while True:
    #talking inputs from player & pc
    print("start game :)")
    player = input("please enter your play (r: for rock , s: for scissors ,p: for paper): ").lower()
    pc = random.choice(["r", "s", "p"])

    #checking if player entered valid input
    while player not in ["r", "s", "p"]:
        print("Invalid input. Please enter 'r', 's', or 'p'.")
        player = input("Please enter your play (r: for rock, s: for scissors, p: for paper): ").lower()

    #displaying both player and pc plays
    print(f"your play: {player}")
    print(f"pc play: {pc}")

    #checking game logic
    if player == pc:
        print(" Tie! ")
    elif rules.get(player) == pc:
        print(" You Won :) ")
    else :
        print(" You lost! :( ")

    #checking if player wants to exit or continue playing
    player_choice = input("Enter [ e ] To Exit or [ r ] T Replay: ").lower()
    if player_choice == "e":
        print("Exiting the game")
        for i in range(10):
            print("."*i)
            time.sleep(0.09)
        print("Done! :)") 
        break
    elif player_choice == "r":
        print("New game") 
    else:
        while player_choice not in ["e","r"]:
            print("Invalid input please Enter [ e ] To Exit or [ r ] T Replay: ")
            player_choice = input("Enter [ e ] To Exit or [ r ] T Replay: ").lower()

