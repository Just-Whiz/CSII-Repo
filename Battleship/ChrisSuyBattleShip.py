# Program Name: 
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 2/4/24
# I pledge my honor

from random import randint

def main():
    """
    This function is the main function. It calls all the other functions in this file.
    """
    print("Welcome to Battleship! Sink your opponents battleships to win!")
    

    turns = 10
    board = generate_gameboard()
    print_board(board)
    ship_coordinates = random_coordinates(board)
    ship_row = ship_coordinates[0]
    ship_col = ship_coordinates[1]

    guesses = guess_coordinates(board, ship_row, ship_col)
    

def guess_coordinates(board, ship_row, ship_col):
    hit = False
    turn = 0
    column_height = len(board)
    row_length = len(board[0])

    while turn < 10:
        guess_row = int(input("What row would you like to fire on? Enter here: "))
        guess_col = int(input("What column would you like to fire on? Enter here: "))
        
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sank my battleship")
            hit == True
        elif (guess_row and guess_col < 0) or (guess_row and guess_col >= column_height) or (guess_row and guess_col <= row_length):
            print("Out of range. Please enter in valid coordinates.")
        elif board[guess_row][guess_col] == "X":
            print("You've already sunk this battleship. Please try some other other coordinates")
        else:
            print("You missed my battleship")
            board[guess_row][guess_col] = "X"
            print_board(board)
            turn += 1
    if hit is True or turn == 10:
        print("Game Over!")


def generate_gameboard():
    """
    This function is the gameboard generator. It generates a 5x5 gameboard every time it is called. It returns 
    the gameboard as an array of arrays (2-Dimensional Array). It 
    
    """
    # Sets the gameboard an array
    board = []

    # For loop that creates the 2-D Array

    for i in range(0, 5):                           # For loop that iterates 5 times
        board.append(["O"]*5)                       # Each iteration, add a new array with 5 "O" strings as the values and add it to the 2-D Array 
    return board                                    # Return the built 2-D Array as an array of arrays

def print_board(board):
    """
    This function prints the gameboard. It prints all the "rows"
    """
    for row in board:
        print(" ".join(row))

def random_coordinates(board):
    """
    This function returns a tuple of random numbers as "randomized" coordinates within the board. 
    They can be accessed via indices through a variable as the values are returned in an array format.
    """
    return [randint(0, len(board) - 1), randint(0, len(board) - 1)]

if __name__ == '__main__':
    main()