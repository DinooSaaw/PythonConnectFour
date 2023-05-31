
### Connect Four Game

This is a simple text-based implementation of the Connect Four game in Python. The game allows two players to take turns and aims to connect four of their game pieces ('X' or 'O') in a row, column, or diagonal on a 6x7 grid.

## How to Play

 1. Run the Python `script connect_four.py.`

 2. The game will display an empty Connect Four board.

 3. Players will take turns entering a column number (0-6) to drop their game piece.

 4. The game will check if the move is valid and update the board accordingly.

 5. The game will continue until one player connects four pieces or the board is full.

 6. The game will display the final board and the winner or declare a draw.

# Example Usage

```
$ python connect_four.py

  

- - - - - - -

- - - - - - -

- - - - - - -

- - - - - - -

- - - - - - -

- - - - - - -

  

Player X, enter a column number (0-6): 3

  

- - - - - - -

- - - - - - -

- - - - - - -

- - - - - - -

- - - X - - -

- - - - - - -

  

Player O, enter a column number (0-6): 2

  

- - - - - - -

- - - - - - -

- - - - - - -

- - - - - - -

- - - X - - -

- - - O - - -

  

...

  

Player X, enter a column number (0-6): 0

  

- - - - - - -

- - - - - - -

- - - - - - -

- - - - - - -

- - - X - - -

X - - O - - -

  

Player X wins!
```
