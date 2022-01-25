# Global importations
import os
from platform import system
from shutil import move
import time
import random

# Define variables
empty_board = [" "," "," "," "," "," "," "," "," "," "]
filled_board = ["1","2","3","4","5","6","7","8","9"]
goal_states = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# Print the header
def print_header():
    print("""
        WELCOME TO SHARIF'S TIC TAC TOE GAME!
    """)

# Define the print board function
def print_board(board):
    print("   |   |   ")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + "  ")
    print("   |   |   ")

    
# Define the AI algorithm
def get_computer_move(board, player):
    # If the center square is empty, choose that
    if board[4] == " ":
        return 4

    while True:
        move = random.randint(0,8)
        # If the move is blank, go ahead and return, otherwise try again
        if board[move] == " ":
            return move
        else: 
            return 4

# Define check player win function
def is_winner(board, player):
    for states_group in goal_states:
        if board[states_group[0]] == player and board[states_group[1]] == player and board[states_group[1]] == player:
            return True
        else:
            return False

# Define check if board is full function
def is_board_full(board):
    if " " in board:
        return False
    else:
        return True


# Driver code
while True:
        os.system("cls")
        print_header()
        print_board(empty_board)

        # Get player X input
        choice = input("Please choose an empty space from 1 to 9 for X.\n")
        choice = int(choice)

        # Check to see if the number is valid
        if (choice > 0 & choice < 10):
            # Check to see if the space is empty
            if empty_board[choice - 1] == " ":
                empty_board[choice - 1] = "X"
            else:
                print("Sorry, that space is not empty!")
                time.sleep(3)
        else:
            print("Please choose a number from 1 to 9.")
            time.sleep(3)

        # Check if X win
        if is_winner(empty_board, "X"):
            os.system("cls")
            print_header()
            print_board(empty_board)
            print("X wins! Congratulations")
            break

        os.system("cls")
        # print_header()
        print_board(empty_board)

        # Check for a tie (is the board full)
        # If the board is full, do something
        if is_board_full(empty_board):
            print("Tie!")
            break

        # Get player O input
        choice = get_computer_move(empty_board, "O")

        # Check to see if the space is empty first
        if empty_board[choice] == " ":
            empty_board[choice] = "0"
        else:
            print("Sorry, that space is not empty!")
            time.sleep(3)

        # Check for O win
        if is_winner(empty_board, "O"):
            os.system("cls")
            print_header()
            print_board(empty_board)
            print("O wins! Congratulations")
            break
        
        # Check for a tie (is the board full)
        # If the board is full, do something
        if is_board_full(empty_board):
            print("Tie!")
            break
