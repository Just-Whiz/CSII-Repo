# Program Name: WIANChrisSuy
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 2/20/24
# I pledge my honor

import time

def main():
    """
    This function is the main function of the program. All other functions below the the ___ line will be called from here.

    Local Variables:
    """
    count = 0
    print("Welcome to the String Analyzer")
    name = str(input("Enter your name: "))
    try:
        go = True
        answer = "Y"
        while go is True:
            time.sleep(1)
            print("""Options:
1) Reverse the display of your name
2) Count vowels
3) Count consanants
          """)
            answer = int(input("Enter your response here: "))
            if answer == 1:
                print("Reversing the display of the name...")
                time.sleep(1)
                reversed_name = reverse_display(name)
                print(reversed_name)
            elif answer == 2:
                print("Determining the vowel count...")
                time.sleep(1)
                print(f"There are {determine_vowel_number(name)} vowels in this name.")
            elif answer == 3: 
                print("Determining the consonant count... ")
                print(f"There are {} consonants in this name")
            elif answer == 4:
                print("Changing name to lowercase...")
                print(f"Your name in lowercase is as follows:{change_to_lowercase(name)}")
            elif answer == 5:
                print("Changing name to uppercase...")
                print(change_to_uppercase(name))
            elif answer == 6:
                print("placeholder")
            elif answer == 7:
                print("placeholder")
            else:
                print("Error. Please enter valid input.")
    except ValueError:
        print("Not a valid input. Please enter a number.")

def reverse_display(x):
    """
    This function is will "reverse" the display of the person's name

    Local Variables:
    """
    return x[::-1]

def isVowel(ch):
    """
    This function is a "helper" function.
    """
    return ch in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def determine_vowel_number(name):
    """
    This function is meant to determine the number of vowels present in a given string. 
    This function will prompt a user for a particular vowel or create subtotals of each.
    Dependent on user input.

    Local Variables:
    """
    count = 0
    for i in range(len(name)):
        if isVowel(name[i]):
            count += 1
    return count

def isConsonant(char):
    """
    This function will determine and filter out all consonants in a name, and filter out all vowels

    Local Variables:
    """
    char = change_to_lowercase(char)

    return not (char == "A" or char == "E" or char == "I" 
                or char == "O" or char == "U") and ord(char) >= 65 and ord(char) <= 90

def totalConsonants(name):
    """
    This function will
    """
    count = 0
    for char in range(len(name)):
        if (isConsonant(name[char])):
            count += 1
    return count

def split(name):
    """
    This function will 
    """
    split_values = []
    temp = ""
    for words in name:
        if words == " ":
            split_values.append(temp)
            temp = ""
        else:
            temp += words
    if temp:
        split_values.append(temp)
    return split_values

def return_first_name():
    """
    This function will return the first name of given name.

    Local Variables:
    """
    name = split(name)

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

def change_to_lowercase(name):
    """
    This function converts letters in a string from uppercase to lowercase by using the ASCII table. It leaves any and all values 
    already in lowercase or non-letter values as is. 

    Local Variables:


    """
    converted_letters = ""
    for char in name:
        if ord(char) >= 65 and ord (char) < 90:
            char = ord(char) + 32
            conversion = chr(char)
            uppercase_letters += conversion
        else:
            uppercase_letters += char
    return uppercase_letters
    

def change_to_uppercase(name):
    """
    This funciton converts letters in a string from lowercase to uppercase by using the ASCII table. It leaves any and all values
    already in lowercase or non-oletter values as is.

    Local Variables:
    char - 
    conversion - 
    converted_letters - 
    """
    for char in name:
        if ord(char) >= 97 and ord(char) < 122:
            char = ord(char) - 32
            conversion = chr(char)
            lowercase_letters += conversion
        else: 
            lowercase_letters += char
    return lowercase_letters

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