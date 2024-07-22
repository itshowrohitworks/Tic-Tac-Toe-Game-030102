### Tic Tac Toe Python Project

This project implements a classic Tic Tac Toe game using Python. The game features the following functionalities:

1. **Game Board Display**:
   - Utilizes the `IPython.display.clear_output` function to refresh the game board display for a clean and interactive user experience.
   - A function `display_board(board)` that prints the current state of the game board.

2. **Player Input**:
   - A function `player_input()` that prompts Player 1 to choose their marker ('X' or 'O') and assigns the opposite marker to Player 2.

3. **Marker Placement**:
   - A function `place_marker(board, marker, position)` that places a player's marker at the specified position on the board.

4. **Win Check**:
   - A function `win_check(board, mark)` that checks if a player has won the game by forming a line of three markers horizontally, vertically, or diagonally.

5. **Random First Player**:
   - A function `choose_first()` that randomly selects which player goes first using the `random.randint()` function.

6. **Space Availability Check**:
   - A function `space_check(board, position)` that checks if a specified position on the board is available.

7. **Full Board Check**:
   - A function `full_board_check(board)` that checks if the board is full, indicating a draw if no player has won.

8. **Player's Move Choice**:
   - A function `player_choice(board)` that prompts the player to choose a position on the board, ensuring the position is valid and available.

9. **Replay Option**:
   - A function `replay()` that asks players if they want to play another game, restarting the game loop if they choose to do so.

10. **Main Game Logic**:
    - A while loop that drives the game, resetting the board, assigning markers, and alternating turns between players until a win or draw condition is met.
    - Prompts for replaying the game after each round.
      
This project demonstrates a structured approach to game development in Python, utilizing functions to manage different aspects of the game, ensuring code readability, and maintainability. It provides a fully interactive command-line experience for playing Tic Tac Toe.
