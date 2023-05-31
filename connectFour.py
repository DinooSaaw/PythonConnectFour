def create_board(rows, columns):
    board = []
    for _ in range(rows):
        row = ['-' for _ in range(columns)]
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_valid_move(board, column):
    return board[0][column] == '-'

def make_move(board, column, player):
    for row in range(len(board) - 1, -1, -1):
        if board[row][column] == '-':
            board[row][column] = player
            return

def is_winning_move(board, row, column, player):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # Only need to check in these four directions
    for dx, dy in directions:
        count = 1
        # Check in both directions (positive and negative)
        for direction in range(2):
            step = 1
            while True:
                new_row = row + step * dx if direction == 0 else row - step * dx
                new_column = column + step * dy if direction == 0 else column - step * dy
                if 0 <= new_row < len(board) and 0 <= new_column < len(board[0]):
                    if board[new_row][new_column] == player:
                        count += 1
                        if count == 4:
                            return True
                    else:
                        break
                else:
                    break
                step += 1
    return False



def is_board_full(board):
    return all('-' not in row for row in board)

def play_connect_four():
    rows = 6
    columns = 7
    board = create_board(rows, columns)
    current_player = 'X'

    while True:
        print_board(board)
        try:
            column = int(input(f"Player {current_player}, enter a column number (0-{columns-1}): "))
            if column < 0 or column >= columns:
                raise ValueError
        except ValueError:
            print("Invalid column number. Please try again.")
            continue

        if is_valid_move(board, column):
            make_move(board, column, current_player)
            if is_winning_move(board, len(board) - 1, column, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. That column is already full.")

play_connect_four()
