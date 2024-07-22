# Tic Tac Toe Game:

**This is a simple project which contains these steps:**
1. *Display Information*
2. *Accepting User Input*
3. *Validating User Input*
4. *Simple User Interaction*

**To start this project, I have to built a Display Board for our Tic Tac Toe Game.**

**For that I imported "clear_output" from the "IPython.display" Library.
The thing is the "clear_output" only works in Jupyter NoteBook on which I developed this game.**

**I created a function that can print out a board named as "display_board".
Then I set up my board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

from IPython.display import clear_output

def display_board(board):
    clear_output()

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

**Testing is also important as it shows wheather we are getting our desired output or not.**

**So I started my very first test to check our "display_board" is working fine or not.**

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

**As it works fine so then we move to create a player input and assign their player_id as "X" or "O".**

*In this process the "while loops" plays a crucial role.*


def player_input():
    player_id = ''

    while not (player_id == 'O' or player_id == 'X'):
        player_id = input('Player 1: Do you want to be O or X? ').upper()

    if player_id == 'O':
        return ('O', 'X')
    else:
        return ('X', 'O')

**Now we will test it for the second time by making sure we get the desired output.**"""

player_input()

*Notice! We only get what the program wanted us to choose as I mistype int(1) in the input panel but the program asked me again the desired output without breaking that's where "while loops" are useful.*

**Now I have created a function that takes in the board list object, a player_id("O" or "X"), and a desired position(from 1 to 9) and assigns it to the board.**


def place_marker(board, marker , position):
    board[position] = marker

**Now we will test our program for the third time to test the parameters and display are working fine or not.**"""

place_marker(test_board,'R',8)
display_board(test_board)

**So here we can see I got the desired outputs with the "python indexing" where,
we get:**

test_board means the test_board

'R' means the marker and

int(8) means the position on which out variable will land.

**Now I have created a function that takes in a board and checks to see if someone has won.**


def win_check(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

**Now we test our program for the forth time to run the win_check function against our test_board - it should return True**"""

win_check(test_board,"X")

**Now I created a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**"""

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

**Now I created a function that returns a boolean indicating whether a space on the board is freely available.**"""

def space_check(board, position):

    return board[position] == ' '

**Now I created a function that checks if the board is full and returns a boolean value.**

True if full, False otherwise.


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

**Now I created a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then return the position for later use.**"""

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

**Now I created a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**"""

def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

**At last I created a full print statement for my display_board!**

*Using while loops and the functions I have made to run the game!*


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

"""**Hence, This is the simple user-interactive "Tic Tac Toe Game" I created using the Python Interface on Jupyter Notebook.**

# Thank you for looking at this Game NoteBook I appreciate your precious time.
"""
