# Program Name: ChrisSuyFileIO.py
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 12/31/23
# I pledge my honor
# Coded: Main, print all students, print all students in grad 12, compare boys vs. girls, find all students with the same last name, find all students with the same first name (+ 
# specific subsequent queries + both functions include NOT FOUND), and adding a tusdent to the directory with queries and appending it ot the current list

from pathlib import Path
import csv
from csv import writer
import time


def main():
    """
    This function is the main. It calls all other functions present below the 48th line.
    
    
    Global Variables:

    file_input - Denotes the variable that open and stores the CSV file in the local directory in "Read" mode

    Local Variables:

    go - Denotes the variable set to True, which allows the while True loop to loop forever, causing the screen to always pop up after
    a function is called and executed
    answer - Denotes the variable that 

    """

    current_dir = Path(__file__).parent
    file_path = current_dir / "gcds_data3.csv"

    go = True
   
    while go is True:
        print('''=================================================================
Menu: Enter Choice or 'Q' to (Q)uit:

1) Print all students at school
2) Count the amount of students in grade 12
3) Compare the amount of boys versus girls
4) Find all students with the same last name (with not found)
5) Find all students with the same first name (with not found)
6) Add a new student entry to the end of the list
=================================================================
''')
        time.sleep(1)
        answer = input("Enter your input here: ")

# The code below is the menu selections with if statements

        if answer == "1": 
            display_all(file_path)
            time.sleep(1)
        elif answer == "2":
            count_seniors(file_path)
            time.sleep(1)
        elif answer == "3":
            compare_genders(file_path)
            time.sleep(1)
        elif answer == "4":
            find_by_last_name(file_path)
            time.sleep(1)
        elif answer == "5": 
            find_by_first_name(file_path)
            time.sleep(1)
        elif answer == "6":
            add_new_entry(file_path)
            time.sleep(1)
        elif answer == "7":
            sort_students(file_path)
            time.sleep(1)
        elif answer == "8":
            update_student_info(file_path)
            time.sleep(1)
        elif answer == "11":
            display_all(file_path)
            time.sleep(1)
        elif answer == "Q" or "q":  	
            print("goodbye")
            time.sleep(1)
            break

def display_all(file_input):

    """
    This function displays all the students/all the data in the given CSV file.
    It first opens the CSV file (gcds_data3.csv), assigns a variable as a reader (reader), defines the
    header (header), and then moves the reader past it, because it is the first line of the document.
    It assigns variable names to each row, and prints all the data present in each of those rows.
    Each variable is stylized with the title present for each of the rows in the file.
    
    Local Variables:
    student_last_name - each student's last name.
    """

    with open(file_input) as file:
        for column in file:
            print(column, end="")
            time.sleep(0.00000000000000001)


def count_seniors(file_input):
    """
    This function displays all the seniors' names that currently go to GCDS. 

    By taking file_input as a variable, (as defined in the main), this function is able to iterate through all the rows
    in the csv file that the variable is attached to (gcds_data3.csv), and singles out each kid whose grade level is
    "Grade 12". For every kid there, it adds one to a variable counter (senior_counter), and then prints to the user
    the number.

    Local Variables:
    record - Denotes the columns 
    row - Denotes the columns and rows and splits them them by the delimiter (in this case, a comma ",")
    senior_counter - Denotes the counter of the amount of students in the 12th Grade
    """
  
    senior_counter = 0                                          # Sets the counter to 0

    with open(file_input) as file:                             # Opens the specified file path stored in the variable
        for record in file:                                   # For 
            column = record.split(",")                            
            if column[2] == "Grade 12":                             # If the 2nd row has this string value:
                time.sleep(0.01)                                    # Delay between counting
                senior_counter += 1                                 # Add 1 to the counter
    
    print(f"There are {senior_counter} seniors.")               # Prints to the user how many seniors there are


def compare_genders(file_input):
    """
    This function counts the amount of girls and boys, and finds who has more numbers in terms of gender.

    By taking file_input as a variable, (as defined in the main), this function is able to iterate through all the rows
    in the csv file that the variable is attached to (gcds_data3.csv), and singles out the third row. While iterating, it 
    looks to see if the value present is "Male" or "Female". If they're either, their respective gender counter goes up by 
    one. Once done, it prints to the user the amount present in each variable gender counter, and prints if there are more
    guys or gals.

    Local Variables:
    males_counter - Denotes the male counter
    females_counter - Denotes the female counter
    """
    males_counter = 0
    females_counter = 0

    file_input.seek(1)                                                  # Moves the pointer to line 1
    with open(file_input) as file:
        for record in file:                                           # Iterates through all those in lines 
            row = record.split(",")
            if row[3] == "Male":                                            # If the iteration encounters this specific string:
                males_counter += 1
            elif row[3] == "Female":                                        # Otherwise if the iteration encounters this specific string:
                females_counter += 1

    print(f"There are {males_counter} guys.")                           # F string to display the value of a variable within a string format
    time.sleep(1)
    print(f"There are {females_counter} girls.")                        # F string to display the value of a variable within a string format
    time.sleep(1)

    males_counter = int(males_counter)                                  # Turns the value in the counter to an integer value
    females_counter = int(females_counter)                              # See above
    gender_difference = abs(males_counter - females_counter)            # Finds the absolute value of the difference b

    if males_counter > females_counter:
        print(f"There are {gender_difference} more guys than gals")
    elif females_counter > males_counter:
        print(f"There are {gender_difference} more gals than guys")

def find_by_last_name(file_input):
    """
    This function finds all kids with the same last name through a simple user prompt. It first asks the user for the last 

    Local Variables:

    query_last - Denotes the variable that stores the "last name" string value the user inputs
    name_counter - Denotes the integer value of the amount of instances the variable query_last was found in

    """

    name_counter = 0

    query_last = input("What is the last name of the student that you're looking for? Enter here: ")

    try:
        with open(file_input) as file: 
            for record in file:
                row = record.split(",")
                if row[0] == query_last:
                        name_counter += 1
                print(f"There are {name_counter} kids with the last name {query_last}")
    except name_counter == 0: 
        print("Person not found within this database")


def find_by_first_name(file_input):
    """
    This function finds kids by first name through a more complex user prompt. 

    Local Variables: 

    query_last - Denotes the variable that stores the "first name" string value the user inputs
    name_counter - Denotes the integer value of the amount of instances the variable query_last was found in
    first_query_name - Denotes the input question of the first variable
    second_query_last_names - Denotes the input quesiton of the second variable
    third_query_gender - Denotes the input question of the third variable
    final_query_address - Denotes the final input question of the fourth variable
    """

    name_counter = 0

    first_query_name = input("What is the first name of the student that you're looking for? Enter here1 for yes, 2 for no: ")
    try:
        with open(file_input) as file:
            for record in file:
                row = record.split(",")
                if row[0] == first_query_name:
                        name_counter += 1
            print(f"There are {name_counter} kids with the last name {first_query_name}")
    except row[0] != first_query_name:
        print("Entry Not Found")

    second_query_last_names = input("Would you like to display the last names of these kids? Enter 1 for yes, 2 for no: ")

    if second_query_last_names == "1":
        print("Just a second...")
        time.sleep(1)
        try:
            with open(file_path) as file_input:
                for record in file_input:
                    row = record.split(",")
                    if row[0] == first_query_name:
                        print(f"{row[0]} {row[1]}")
                    print("Goodbye")
        except row[0] != first_query_name:
            print("Entry Not Found")

    third_query_gender = input("Would you like the genders of all the people in this list? Enter 1 for yes, 2 for no: ")
    
    if third_query_gender == "1":
        print("just a second...")
        time.sleep(1)
        with open(file_path) as file_input:
            for record in file_input:
                row = record.split(",")
                if row[0] == first_query_name:
                    print(f"{row[0]} {row[1]}. Gender: {row[3]}")


def add_new_entry(file_path):
    """
    This function adds a new entry (in this case, a new student) to the file as a whole. To add a completely new entry,
    the funciton will ask the user for the first name, last name, grade, gender, town, and state that the student lives in.

    Local Variables: 
    first_name_query - 
    last_name_query
    grade_query - 
    gender_query - 
    address_query - 
    city_query - 
    state_query - 
    file_write - 
    writer_object - 
    """
    
    print("You've chosen to add a new student entry.")
    time.sleep(1)
    try:
        first_name_query = input("What is the student's first name? Enter here: ")
        last_name_query = input("What is the student's last name?")
        grade_query = input("What is the student's current grade? Enter here: ")
        gender_query = input("What does the student identify as? Enter here:")
        address_query = input("What is the student's address? Enter here: ")
        city_query = input("What city does the student live in? Enter here: ")
        state_query = input("What state does the student live in? Please only use 2-letter acronyms; Enter here: ")

        grade_query = int(grade_query)


        appendage_list = [first_name_query, last_name_query, grade_query, gender_query, address_query, city_query, state_query]

        with open(file_path, "a") as file_write:
            writer_object = writer(file_write)
            writer_object.writerow(appendage_list)
            file_write.close()
    except grade_query != int(grade_query) or len(state_query) > 2:
        print("Invalid entries. Please try again with valid entries.")

def sort_students(file_input):
    """
    This function lists students by first name, last name, sorted by lastname. If the user wishes, additional criteria can also
    be displayed as a seperate iteration
    Format: Last name, first name

    Local Variables:

    """

    query_first = input("This function alphabetizes students. Would you like to ")
    print("placeholder")


def update_student_info(file_input):
    """
    This function updates a student info based on given criteria. It first asks for the last and first name of the student that you would
    like to change. It then gives you 5 options to choose from: 1) Change the first name of the student 2) Change the last name of the student
    3) Change the grade of the student 4) Change the town the student is from 5) Change the state the student is from. Once done, it replaces the 
    existing information in the csv file and closes the datafile. 

    Local Variables:

    """

    print("placeholder")


def delete_student_info(file_input):
    """
    This function deletes a student's information from the directory. It first asks if the user would like to delete ALL data, or PARTS of the data.

    """

    print("placeholder")

if __name__ == '__main__':
    main()