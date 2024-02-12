# Program Name: ChrisSuyFileIO.py
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 12/31/23
# I pledge my honor

from time import sleep

def main():
    """
    This function is the main function of the program. All other functions below this will be called from here.
    """
    vowels = ["a", "e", "i", "o", "u"]
    count = 0


    print("Welcome to the String Analyzer")

    vowels = input()
    try:
        print("""Options:
1) Print name
2) Count vowels
3) Count consanants
          """)
        go = True
        answer = "Y"
        while go is True:
            answer = int(input("Enter your response here: "))
            if answer == 1:
                print("placholder")
            elif answer == 2:
                print("placeholder")
            elif answer == 3: 
                print("placeholder")
    except ValueError:
        print("Not a valid input. Please enter a number.")

def reverse_display():
    """
    This function is will "reverse" the display of the person's name

    Local Variables:
    """
    first_name = ""
    for i in range(len(name) - 1):
        if name[i] != " ":
            first_name = name[i]
        else:
            return i

def determine_vowel_number():
    """
    This function is meant to determine the number of vowels present in a given string. 
    This function will prompt a user for a particular vowel or create subtotals of each.
    Dependent on user input.

    Local Variables:
    """

def find_consonant_frequency():
    """
    This function will lorem ipsum. It will also create subtotals of each.

    Local Variables:
    """

def return_first_name():
    """
    This function will return the first name of given name.

    Local Variables:
    """

def return_last_name():
    """
    This function will return the last name of the given name.

    Local Variables:
    """

def return_middle_names():
    """
    This function will return the middle name(s) of the given name, if any are present.

    Local Variables:
    """

def find_hyphen():
    """
    This function will check if the last name has a hyphen. 
    If the name has a boolean, then it will return a boolean. 

    Local Variables:
    """

def convert_to_lowercase():
    """
    This function will convert the full given name to lowercase. 

    Local Variables:
    """

def convert_to_uppercase():
    """
    This function will convert the full given name to uppercase.

    Local Variables:
    """

def randomize_name():
    """
    This function modifies the name array to create a random name by mixing up the letters. 

    Local Variables:
    """

def find_palindrome():
    """
    This function returns the full name as a sorted array of characters.

    Local Variables:
    """

def build_menu():
    """
    This function builds a menu. Nothing else to it.

    Local Variables:
    """

def find_initials():
    """
    This function finds the initials of a given name and returns the letters. 

    Local Variables:
    """

def find_titles():
    """
    This function finds if a person's name carries a distinction.

    Local Variables:
    """

if __name__ == '__main__':
    main()