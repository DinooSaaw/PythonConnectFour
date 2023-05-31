import itertools
import tkinter as tk
from tkinter import messagebox

def create_board(rows, columns):
    # Create an empty game board with specified number of rows and columns
    board = []
    for _ in range(rows):
        row = ['-' for _ in range(columns)]
        board.append(row)
    return board

def print_board(board):
    # Print the current state of the game board
    for row in board:
        print(' '.join(row))
    print()

def is_valid_move(board, column):
    # Check if a move is valid (the top row of the specified column is empty)
    return board[0][column] == '-'

def make_move(board, column, player):
    # Make a move by placing a player's token in the specified column
    for row in range(len(board) - 1, -1, -1):
        if board[row][column] == '-':
            board[row][column] = player
            return

def is_winning_move(board, row, column, player):
    # Check if the latest move results in a win for the player
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # Check in all four directions
    for dx, dy in directions:
        count = 1
        winning_squares = [(row, column)]
        for step in range(1, 4):
            new_row = row + step * dx
            new_column = column + step * dy
            if not 0 <= new_row < len(board) or not 0 <= new_column < len(board[0]):
                break
            if board[new_row][new_column] != player:
                break
            count += 1
            winning_squares.append((new_row, new_column))
        if count >= 4:
            return winning_squares

    # Additional check for diagonal in the opposite direction
    for dx, dy in directions[-2:]:
        count = 1
        winning_squares = [(row, column)]
        for step in range(1, 4):
            new_row = row - step * dx
            new_column = column - step * dy
            if not 0 <= new_row < len(board) or not 0 <= new_column < len(board[0]):
                break
            if board[new_row][new_column] != player:
                break
            count += 1
            winning_squares.append((new_row, new_column))
        if count >= 4:
            return winning_squares

    return []

def update_gui():
    # Update the GUI to reflect the current state of the game board
    for i, j in itertools.product(range(len(board)), range(len(board[0]))):
        if (i, j) in winning_squares:
            buttons[i][j].config(state='disabled')
        else:
            buttons[i][j].config(text='-', state='normal')

def restart_game():
    # Restart the game by resetting the board and current player
    global board, current_player, winning_squares
    for row_buttons in buttons:
        for button in row_buttons:
            button.config(text='-', state='normal')
    board = create_board(rows, columns)
    current_player = 'X'
    winning_squares = []
    status_label.config(text=f"Player {current_player}'s turn")

def button_click(row, column):  # sourcery skip: extract-method
    # Handle button click event
    global current_player, winning_squares, player_wins

    if is_valid_move(board, column):
        make_move(board, column, current_player)
        buttons[row][column].config(text=current_player, state='disabled')

        if winning_squares := is_winning_move(board, row, column, current_player):
            # If the current move results in a win
            status_label.config(text=f"Player {current_player} wins!")
            update_gui()
            player_wins[current_player] += 1
            win_count_label.config(text=f"Player X: {player_wins['X']}  Player O: {player_wins['O']}")
            if messagebox.askyesno("Game Over", f"Player {current_player} wins! Do you want to play again?"):
                restart_game()
            else:
                root.destroy()
            return

        if all('-' not in row for row in board):
            # If all cells are filled and there is no winner (draw)
            status_label.config(text="It's a draw!")
            if messagebox.askyesno("Game Over", "It's a draw! Do you want to play again?"):
                restart_game()
            else:
                root.destroy()
            return

        # Switch to the other player's turn
        current_player = 'O' if current_player == 'X' else 'X'
        status_label.config(text=f"Player {current_player}'s turn")


# GUI setup
rows = 6
columns = 7
board = create_board(rows, columns)
current_player = 'X'
winning_squares = []
player_wins = {'X': 0, 'O': 0}

root = tk.Tk()
root.title("Connect Four")
icon_path = "./assets/icon.png"
icon_image = tk.PhotoImage(file=icon_path)
root.iconphoto(True, icon_image)

buttons = []
for i in range(rows):
    row_buttons = []
    for j in range(columns):
        button = tk.Button(root, text='-', width=4, height=2,
                           command=lambda r=i, c=j: button_click(r, c))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

status_label = tk.Label(root, text=f"Player {current_player}'s turn")
status_label.grid(row=rows, columnspan=columns)

win_count_label = tk.Label(root, text="Player X: 0  Player O: 0")
win_count_label.grid(row=rows + 1, columnspan=columns)

root.mainloop()
