from time import sleep

def main():
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
    This function is meant to lorem ipsum.

    Local Variables:
    """
    print("placeholder")

def determine_vowel_number():
    """
    This function is meant to determine the number of vowels present in a given string. 
    This function will prompt a user for a particular vowel or create subtotals of each.
    Dependent on user input.

    Local Variables:
    """
    print("placeholder")

def find_consonant_frequency():
    """
    This function will lorem ipsum. It will also create subtotals of each.

    Local Variables:
    """

def return_first_name():
    """
    This function will return 
    """


if __name__ == '__main__':
    main()