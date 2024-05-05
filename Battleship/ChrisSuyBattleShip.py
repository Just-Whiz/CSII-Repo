# Program Name: ChrisSuyBattleShip
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 5/1/24
# I pledge my honor

from random import randint

def main():
    """
    This function is the main function. It calls all the other functions in this file to make the game playable.

    Functions called: 
    generate_gameboard(): Prints out a 2D array (an array of arrays) as the gameboard
    print_board(board): Prints the value of a variable out to the terminal as readable text
    random_coordinates(): Picks a random value to place the ship on and returns a tuple value as coordinates
    start_game(board, ship_row, ship_col): Takes in the gameboard, and the hidden ship's coordinates as arguments to run the game loop

    Local Variables:
    turns: The turn counter.
    board: The "helper" variable that contains the gameboard, which is then passed in as an argument to the start_game function
    the print_board and random_coordinates() function
    ship_coordinates: the "helper" variable that places the hidden "battleship" on the board
    ship_row: a "helper" variable that takes the 1st tuple value of ship_coordinates, which is then passed in as an argument to the start_game function
    ship_col: a "helper" variable that takes the 2nd tuple value of ship_coordinates, which is then passed in as an argument to the start_game function
    guesses: the variable that "stores" the current game once called
    """                                     
    board = generate_gameboard()                                                                        # Generates the gameboard
    print_board(board)                                                                                  # Prints the gameboard to the terminal
    ship_coordinates = random_coordinates(board)                                                        # Retrives the randomized coordinates the hidden battleship will be placed on and assigns it to a variable
    ship_row = ship_coordinates[0]                                                                      # Assigns the ship's row to the 1st from the ship_coordinate variable
    ship_col = ship_coordinates[1]                                                                      # Assigns the ship's column the 2nd tuple value from the ship_coordinate variable

    print("Welcome to Battleship! Sink the hidden ship to win.")                                        # Prints a statement
    guesses = start_game(board, ship_row, ship_col)                                                     # Starts the game
    
def start_game(board, ship_row, ship_col):
    """
    This function is the function where the game is played from. It is called once from the main function to initiate the game. 
    
    It takes in 3 arguments: the board, and the hidden ship's coordinates as 2 values, ship_row (the hidden ship's location on the "x" axis of gameboard),
    and ship_col (the hidden ship's location on the "y" axis of the gameboard). These are referenced in the loop to determine whether the player
    has hit or not hit the hidden battleship on the board. If the player does hit the battleship, or runs out of turns and does not hit it, game over text
    will run and the player will be asked to retry or to end the loop

    Local Variables:
    board: Contains the gameboard. Passed in as an argument from the main function. Referenced to mark the player's guesses (which include misses and hits)
    ship_row: The hidden battleship's position on the "x" axis of the gameboard (in the list of lists). Passed in as an argument from the main function. Referenced to determine the ship's
    vertical position on the board
    ship_col: The hidden battleship's position on the "y" axis of the gameboard (in the list of lists). Passed in as an argument from the main function. Referenced to determine the ship's
    horizontal position on the board
    hit: A variable that determines whether or not the battleship in question has been hit. While it remains false, run the game until it turns true, in which the player will then determine
    to continue or end the game (the program)
    turns: Contains the amount of turns the player has left. Play until this number reaches 0, in which the player will then determine to continue or end the game (the program)
    guess_row: A variable that stores the current player's guess to the whereabouts of the battleship on the "x" axis of hte gameboard. Determined via input from the player. Referenced to find 
    whether the player has hit the ship or not.
    guess_col: A variable that stores the current player's guess to the whereabouts of the battleship on the "x" axis of hte gameboard. Determined via input from the player. Referenced to find 
    whether the player has hit the ship or not.
    """
    hit = False                                                                                         # Hit is set to false
    turns = 10                                                                                          # The turn counter for the game

    while turns >= 0 or hit:                                                                            # Run until the player runs out of turns or hit is True
        if hit == True or turns == 0:                                                                   # If the player's run out of turns:
            print("Game Over!")                                                                         # Prints a statement
            retry = input("Would you like to play again? Enter Y for Yes, or N for no: ").upper()       # Ask the player if they would like to play again
            if retry == "Y" or "YES":                                                                   # If they would like to play again
                turns = 10                                                                              # Reset both the hit and turns variables back to their initial configurations
                hit = False                                                                             # to restart the game
                print("Welcome to Battleship! Sink the hidden shihp to win.")                           # Prints a statement
            elif retry == "N" or "NO":                                                                  # Otherwise if the player doesn't want to play again
                print("Goodbye!")                                                                       # Prints a statement
                break                                                                                   # End the game and the program
            else:                                                                                       # Otherwise:
                 print("Error. Please enter Y or N as your answer. ")                                   # Ask the user to enter in a valid answer
                 continue                                                                               # Iterates through the loop again
        try:                                                                                            
            print(f"You have {turns} turns left. ")                                                     # Inform the player of the amount of turns they have left

            guess_row = int(input("What row would you like to fire on? Enter here: "))                  # Asks the player for their desired coordinates to fire on. They're entered as integer values.
            guess_col = int(input("What column would you like to fire on? Enter here: "))               # If they're anything other than that, then refer to the ValueError.
                
            guess_row -= 1                                                                              # To account for list accessing/retrieval, 1 is subtracted from each guess so that the correct
            guess_col -= 1                                                                              # "coordinates" (or list locations) are changed (ex: guess_row having a value of 5 corresponds to row[4] not row[5] which would be out of bounds)

            if guess_row == ship_row and guess_col == ship_col:                                         # If the player guesses the ship's column and row location (its coordinates)
                print("Congratulations! You sank my battleship")                                        # Prints a statement
                board[guess_row][guess_col] = "X"                                                       # Changes the coordinate value that was "fired" on to appear as a hit
                hit == True                                                                             # Set both the hit and turns variables to 0 to end the loop (and by proxy, the game itself)
                turns = 0                                                                               
            elif (guess_row < 0 or guess_row >= 5) or (guess_col < 0 or guess_col >= 5):                # If the row and column guesses for the ship are out of range of the board (being 5x5)
                print("These coordinates are out of range. Please enter in valid coordinates.")         # Prints a statement
            elif board[guess_row][guess_col] == "M":                                                    # If the board has already been fired on
                print("You've already fired at this area. Please try some other other coordinates")     # Prints a statement
            else:                                                                                       # Otherwise
                print("You missed my battleship")                                                       # Prints a statement
                board[guess_row][guess_col] = "M"                                                       # Changes the coordinate value that was "fired" on to appear as a miss
                print_board(board)                                                                      # Retrieve the current board's state
                turns -= 1                                                                              # Subtract a turn 
        except ValueError:                                                                              # If there is an issue with values
            print("Error. Please enter numbers.")                                                       # Inform the user to enter valid input
            continue                                                                                    # Iterate through the whole loop again

def generate_gameboard():
    """
    This function is the gameboard generator. It generates a 5x5 gameboard every time it is called. It returns 
    the gameboard as an array of arrays (2-Dimensional Array. It fills each grid with a string filled with "O" strings,
    (not 0's), appends all of them to board's list, and returns the board with all 5 of the appended lists as itself.
    
    Local Variables:
    board: The gameboard variable (passed in as an argument and returned as a variable)
    i: A temporary variable that allows the for loop to loop 5 times
    """
    board = []                                                                                          # Sets the gameboard an array

    for i in range(0, 5):                                                                               # For loop that iterates 5 times
        board.append(["O"]*5)                                                                           # Each iteration, add a new array with 5 "O" strings as the values and add it to the 2-D Array 
    return board                                                                                        # Return the built 2-D Array as an array of arrays

def print_board(board):
    """
    This function prints the gameboard. It prints all the "rows" in the 2D array to the terminal.
    It takes in a variable as an argument (board), which is the gameboard, and prints each row out from the gameboard
    out to be displayed "2-Dimensionally" within the terminal.

    Local Variables
    row: A temporary variable that describes all the lists in the gameboard list (or array if you will), 
    and allows the for loop to loop for as many items there are in board


    """
    for row in board:                                                                                   # For each "row" (every list in the generated board)
        print(" ".join(row))                                                                            # Use the join method on every row (every array in the board) to convert each list values into strings,
                                                                                                        # then to format them with a seperator and print them to the terminal (in this case, 
                                                                                                        # format each "O" value with a space between each value once printed)

def random_coordinates(board):
    """
    This function returns a tuple of random numbers in a 1D array as "randomized" coordinates within the board that 
    can be accessed via indices through a variable as the values are returned in an array format.
    It uses the randint() function from the random library to select a value between 0 and the length of the board. 
    1 is then subtracted in order to account for array accessing (which starts at 0) and to prevent out-of-bounds coordinates
    from being generated.
    """
    return [randint(0, len(board) - 1), randint(0, len(board) - 1)]                                     # Uses randint to get a random value between 0, the length of the board (which is 5) and subtracts 1 to account for list accessing

if __name__ == '__main__':
    main()