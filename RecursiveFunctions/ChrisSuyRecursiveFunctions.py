# Program Name: ChrisSuyFileIO.py
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 12/31/23
# I pledge my honor

import time as sleep

def main():
    """
    This is the main function of the file. It calls all other functions in the file from here.
    """

    print("""Hello World!
          1) Factorial
          2) Summation
          3) Powers
          4) Sum of digits
          5) Fibonacci
          6) Greatest Common Divisor (GCD)
          7) Compound Interest
          
          
           Test the functions here!""")
    try: 
        choice = input("Enter your number choice here: ")
        number = input("Which number number would you like to test?")
        if choice == 1:
            factorial(number)
        elif choice == 2:
            sleep(1)
            summation(number)
        elif choice == 3: 
            sleep(1)
            powers, 
        elif choice == 4:
            sleep(1)
        elif choice == 5:
            sleep(1)
        elif choice == 6:
            sleep(1)
        elif choice == 7:
            sleep(1)
    except ValueError:
        print("Error. Please enter numbers.")
    



def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number for which factorial is to be calculated.
    
    Returns:
    int: The factorial of the given number
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def summation(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number for which the summation is to be calculated

    Returns:
    int: The summation of the given number
    """
    if n == 0:
        return 1
    else:
        return n + summation(n-1)
    
def powers(a, n):
    if n == 0:
        return 1
    else:
        return a * powers(a, n-1)

def sumofdigits(n):
    """
    
    Parameters:

    Returns:

    """
    if n < 10:
        return n
    else:
        return n % 10 + sumofdigits(n/10)

def fibonacci(n):
    """
    Finds the nth value of a number in the fibonacci sequence.

    Parameters:

    Returns: 
    """

    if n <= 1:
        return n
    elif n == 2:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

def GCD(a, b):
    """
    Returns the greatest common divisor of a and b using Euclid's algorithm.

    Parameters:

    Returns:
    
    """
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
def compound_interest(p, r, t):
    """
    
    Parameters: 
    p (int): The principal
    r (int): The rate
    t (int): The time

    """
    if t == 0:
        return p
    else:
        return compound_interest(p * (1 + r), r, t -1)

def product(x, y):
    """
    Parameters:

    Returns:
    
    """
    if x < y:
        return product(y, x)
    elif y != 0:
        return (x + product(x, y - 1))

def reverse_digits(n):
    """
    
    Parameters:

    Returns:

    """
    if n < 10:
        return n
    else:
        return (n % 10) * (10 ** len(str(n // 10))) + reverse_digits(n // 10)

def newtons_algorithm(n, p, e):
    """

    Parameters

    Returns:


    """