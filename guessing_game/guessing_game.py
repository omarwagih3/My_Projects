import random
import time

attempts_list = []
attempts =0

#showing score function
def show_score():
    if not attempts_list :
        print("NO high scores yet! :(")
    else:
        print(f"the highest score is with {min(attempts_list)} attempts")    

#greeting user 
print("Welcome to the Guessing game!")
player_name = input("what's your name?  ")
player_dissection = input(f"hello,{player_name} ,do you want to Guess?  enter (yes / no): ").lower()
random_num = random.randint(1,10)

#starting guessing
while player_dissection == "yes":
    try:
        player_num = int(input("enter number between (1 and 10)<---  "))

        if player_num < 1 or player_num > 10:
            raise ValueError("use number in givin range!")

        elif player_num <= 1 or player_num <= 10:
            attempts += 1
            pc_num = random_num
            if player_num == pc_num:
                print("Right Guessing! :)")
                attempts_list.append(attempts)
                show_score()
                player_dissection = input(f"{player_name} ,do you want to replay?  enter (yes / no): ").lower()
                if player_dissection == "no":
                    print("have a nice day goodbye :)")
                else:
                    attempts = 0
                    random_num = random.randint(1,10)
                    show_score()
                    continue

            elif player_num < pc_num:
                print("Higher Try Again!")  
            elif player_num > pc_num:
                print("Lower Try Again!")  

    except ValueError as err:
        print(err)

    if player_dissection == "no":
        print("Exiting game ...")
        for i in range(8):
            print("."*i)
            time.sleep(0.3)
        show_score()
        print("Done")
        break              
            



