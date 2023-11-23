import random

class GuessingGame:
    """
    A class representing a simple guessing game.
    """

    def __init__(self):
        """
        Initializes the game by setting up the attempts list and prompting the player for their name.
        """
        self.attempts_list = []
        self.player_name = input("What's your name? ")

    def show_score(self):
        """
        Displays the best score achieved by the player.
        """
        if not self.attempts_list:
            print("No high scores yet! :(")
        else:
            print(f"The best score is {min(self.attempts_list)} attempts")

    def play(self):
        """
        Initiates the game and handles the game loop.
        """
        play_again = "yes"

        while play_again.lower() == "yes":
            attempts = 0
            random_num = random.randint(1, 10)

            valid_input = False
            while not valid_input:
                player_input = input("Enter a number between 1 and 10: ")
                if player_input.isdigit():
                    player_num = int(player_input)
                    if 1 <= player_num <= 10:
                        valid_input = True
                    else:
                        print("Please enter a number within the given range!")
                else:
                    print("Please enter a valid number!")

            attempts += 1

            if player_num == random_num:
                print("Correct guess! :)")
                self.attempts_list.append(attempts)
                self.show_score()
                play_again = input(f"{self.player_name}, do you want to play again? Enter (yes / no): ")
            elif player_num < random_num:
                print("Try a higher number!")
            else:
                print("Try a lower number!")

            if play_again.lower() == "no":
                print("Exiting game...")
                self.show_score()
                print("Done")

game = GuessingGame()
game.play()
