# Program Name: 
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 2/4/24
# I pledge my honor

import time
import sys
import pygame
import random

pygame.init()

#my_sound = pygame.mixer.Sound("Path/to/my/soundfile.wav")
#my_sound.play()

def main():
    print("Welcome to Battleship!")
    setUpGame()

def setUpGame():
    gameBoard = generateArray()
    for row in gameBoard:                                                                                 # Prints all values in the array out
        print(row)


def generateArray():
    """
    This function generates gameboard arrays. 

    First, it assigns rows and cols a value of 10 (to create a 10 by 10 grid) in order to create an array/grid.
    Then, the array (referenced as the variable arr) is created with two for loops, one to create the columns of the array,
    and the other to create the rows, all filled with 0's to represent 

    Local Variables:

    """
    rows, cols = (10, 10)

    arr = [[0] * cols for i in range(rows)]
    return arr


if __name__ == "__main__":
    main()
