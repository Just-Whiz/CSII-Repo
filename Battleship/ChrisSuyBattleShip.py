# Program Name: 
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 2/4/24
# I pledge my honor

import time
import sys
import random


def main():
    print("Welcome to Battleship!")
    generateArray()

def generateArray():
    rows, cols = (10, 10)

    arr = [[0 for i in range(cols)] for j in range(rows)]
    for row in arr:
        print(row)

def print1by1(text, delay=0.015):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print

if __name__ == "__main__":
    main()
