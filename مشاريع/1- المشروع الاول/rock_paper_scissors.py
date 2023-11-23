# Start the game
# Ask the player to make a move (r, p, s)
# PC would select a move radomly
# PC == Player -> Tie
# (Player == P and PC == Rock) or (Player == R and PC == Scissors) or (Player == Scissors and PC == Paper)
## User won / You won
# Any other case
## PC won / You lose

import random

user = input("What's your choice? 'r' for Rock, 'p' for Paper, and 's' for Scissors\n")
pc = random.choice(['r', 'p', 's'])

print("User played: " + user)
print("PC played: " + pc)

if user == pc:
    print("It's a tie!")
elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
    print("You won!")
else:
    print("You lose!")

