import tkinter as tk  # Import the tkinter module for GUI
import random  # Import the random module for computer moves

class TicTacToe:
    def __init__(self, root):
        self.root = root  # Initialize the main window
        self.root.title("Tic Tac Toe")  # Set the title of the window

        self.turn = "X"  # Initialize the player's turn
        self.board = [" " for _ in range(9)]  # Create the game board
        self.player_score = 0  # Initialize player's score
        self.computer_score = 0  # Initialize computer's score

        # Create and display the score label
        self.score_label = tk.Label(self.root, text=f"You: {self.player_score} Computer: {self.computer_score}", font=("Arial", 12))
        self.score_label.grid(row=0, column=0, columnspan=3)

        # Create and display the result label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.result_label.grid(row=1, column=0, columnspan=3)

        # Create and display the restart button
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart)
        self.restart_button.grid(row=2, column=0, columnspan=3)

        # Create the game buttons and display them on the grid
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=("Arial", 20), width=5, height=2, command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i+3, column=j)
                self.buttons.append(button)

    # Method to handle button click
    def on_button_click(self, i, j):
        index = 3 * i + j
        if self.board[index] == " ":
            self.board[index] = self.turn
            self.buttons[index].config(text=self.turn)
            if self.check_winner(self.turn):
                self.show_winner(self.turn)
                self.disable_buttons()
            elif all(cell != " " for cell in self.board):
                self.show_winner("Tie")
                self.highlight_tie()
            else:
                self.turn = "O" if self.turn == "X" else "X"
                if self.turn == "O":
                    self.computer_move()

    # Method for computer's move
    def computer_move(self):
        available_moves = [i for i, cell in enumerate(self.board) if cell == " "]
        if available_moves:
            index = random.choice(available_moves)
            self.on_button_click(index // 3, index % 3)

    # Method to check for a winner
    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i*3 + j] == player for j in range(3)) or all(self.board[i + j*3] == player for j in range(3)):
                return True
        if all(self.board[i*4] == player for i in range(3)) or all(self.board[2 + i*2] == player for i in range(3)):
            return True
        return False

    # Method to display the winner
    def show_winner(self, winner):
        if winner == "Tie":
            label_text = "It's a Tie!"
        else:
            label_text = f"{winner} wins!"
            if winner == "X":
                self.player_score += 1
            elif winner == "O":
                self.computer_score += 1
            self.score_label.config(text=f"You: {self.player_score} Computer: {self.computer_score}")
        self.result_label.config(text=label_text)

    # Method to disable all buttons
    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    # Method to restart the game
    def restart(self):
        self.turn = "X"
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ", state="normal")
        self.result_label.config(text="")

          # Reset tie highlight
        self.highlight_tie(False)

    # Method to highlight a tie
    def highlight_tie(self, highlight=True):
        color = "red" if highlight else "SystemButtonFace"
        for button in self.buttons:
            button.config(bg=color)

  # Create the main window
root = tk.Tk()

 # Initialize the game
game = TicTacToe(root)

  # Start the game loop
root.mainloop()
