# Program Name: ChrisSuyFileIO.py
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 10/6/23
# I pledge my honor
# Running bug list: None to report at the moment.
# To be coded: Make complex selections (first by gender, then city, then by amount of specific grade living there), make selections from database (e.g. ask first name, gender, grade to find specific student), 

from pathlib import Path
import csv
import time

def main():
    """
    This function is the main. It calls all other functions present below the 48th line.
    """
    file_input = open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r')

    file_input.readline()                       # Skip first line of header info
    answer = "Y"
    go = True

   
    while go is True:
        print('''=================================================================
Menu: Enter Choice or 'Q' to (Q)uit:

1) Print all students at school
2) Print all students in grade 12
3) Compare the amount of boys versus girls
4) Find all students with the same first name (with not found)
6) Add a student to the end of the list
=================================================================
''')
        time.sleep(1)
        answer = input("Enter your input here: ")

# The code below is the menu function logic

        if answer == "1":
            display_all(file_input)
            time.sleep(1)
        elif answer == "2":
            count_seniors(file_input)
            time.sleep(1)
        elif answer == "3":
            compare_genders(file_input)
            time.sleep(1)
        elif answer == "4":
            find_by_first_name(file_input)
            time.sleep(1)
        elif answer == "5": 
            find_by_last_name(file_input)
            time.sleep(1)
        elif answer == "6":
            add_new_entry(file_input)
            time.sleep(1)
        elif answer == "7":
            sort_students(file_input)
            time.sleep(1)
        elif answer == "8":
            update_student_info(file_input)
            time.sleep(1)
        elif answer == "11":
            display_all(file_input)
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

    file_input.seek(1)

    for record in file_input: 
        row = record.split(",")
        time.sleep(0.00000000001)
        print(row[1], row[0], row[2], row[3], row[4], row[5], row[6])

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
    
    file_input.seek(1)                                          # Moves pointer to line 1
    senior_counter = 0                                          # Sets the counter to 0

    for record in file_input:                                   # For 
        row = record.split(",")                            
        if row[2] == "Grade 12":                                # If the 2nd row has this string value:
            time.sleep(0.01)                                    # Delay between counting
            senior_counter += 1                                 # Add 1 to the counter
    
    print(f"There are {senior_counter} seniors.")               # Prints to the user how many seniors there are
    time.sleep(1)

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

    file_input.seek(1)                                          # Moves the pointer to line 1

    for record in file_input:                                   # Iterates through all those in lines 
        row = record.split(",")
        if row[3] == "Male":                                    # If the iteration encounters this specific string:
            males_counter += 1
        elif row[3] == "Female":                                # Otherwise if hte iteration encounters this specific string:
            females_counter += 1

    print(f"There are {males_counter} guys.")                   # F string to display the value of a variable within a string format
    time.sleep(1)
    print(f"There are {females_counter} girls.")                # F string to display the value of a variable within a string format
    time.sleep(1)

    males_counter = int(males_counter)                          # Turns the value in the counter to an integer value
    females_counter = int(females_counter)                      # See above
    gender_difference = abs(males_counter - females_counter)    # Finds the absolute value of the difference b

    if males_counter > females_counter:
        print(f"There are {gender_difference} more guys than gals")
    elif females_counter > males_counter:
        print(f"There are {gender_difference} more gals than guys")
    time.sleep(1)

def count_by_zip(file_input):
    """
    This function counts how many kids live in each city (e.g. through a convenient menu of simple selection). It first gives
    the user the amount of 
    """

    
    for record in file_input:                           #Iterates through all those in lines 
        row = record.split(",")
        if row[3] == "Male":
            males_counter += 1
        elif row[3] == "Female":
            females_counter += 1

def find_by_first_name(file_input):
    """
    This function finds all kids with the same first name through a simple user prompt.

    Local Variables:

    """

    print("placeholder")

def find_by_last_name(file_input):
    """
    This function finds kids by last 

    Local Variables: 

    """

    print("placeholder")

def add_new_entry(file_input):
    """
    This function adds a new entry (in this case, a new student) to the file as a whole. To add a completely new entry,
    the funciton will ask the user for the first name, last name, grade, gender, town, and state that the student lives in.

    Local Variables: 

    """

    print("placeholder")

def sort_students(file_input):
    """
    This function lists students by first name, last name, sorted by lastname. If the user wishes, additional criteria can also
    be displayed as a seperate iteration
    Format: Last name, first name

    Local Variables:

    """

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



