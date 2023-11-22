# Program Name: ChrisSuyFileIO.py
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 10/6/23
# I pledge my honor

import csv
import time

def main():
    """
    This function is 
    """
    file_input = open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r')

    file_input.readline()                       #skip first line of header info
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

# The code below is the menu function

        if answer == "1":
            display_all(file_input)
            time.sleep(1)
        elif answer == "2":
            count_seniors(file_input)
            time.sleep(1)
        elif answer == "3":
            compare_genders(file_input)
        elif answer == "7":
            display_all(file_input)
            time.sleep(1)

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
        print(row[1], row[0], row[2], row[3], row[4], row[5])



def count_seniors(file_input):
    """
    This function displays all the seniors' names that currently go to GCDS. 

    By taking file_input as a variable, (as defined in the main), this function is able to iterate through all the rows
    in the csv file that the variable is attached to (gcds_data3.csv), and singles out each kid whose grade level is
    "Grade 12". For every kid there, it adds one to a variable counter (senior_counter)

    Local Variables:
    record - Denotes the columns 
    row - Denotes the columns and rows and splits them them by the delimiter (in this case, a comma ",")
    senior_counter - Denotes the counter of the amount of students in the 12th Grade
    """
    
    file_input.seek(1)                                     # Moves pointer to line 1
    senior_counter = 0                                     # Sets the counter to 0

    for record in file_input:                              # For 
        row = record.split(",")                            
        if row[2] == "Grade 12":                           # If the 2nd row has this string value:
            time.sleep(0.01)                               # Delay between counting
            senior_counter += 1                            # Add 1 to the counter
    
    print(f"There are {senior_counter} seniors.")          # Prints to the user how many seniors there are
    time.sleep(1)



def compare_genders(file_input):
    """
    This function counts the amount of girls and boys, and finds who has more numbers in terms of gender.

    By taking file_input as a variable, (as defined in the main), this function is able to iterate through all the rows
    in the csv file that the variable is attached to (gcds_data3.csv), and singles out the third row as the row 

    Local Variables:
    males_counter - Denotes the male counter
    females_counter - Denotes the female counter
    """
    males_counter = 0
    females_counter = 0

    file_input.seek(1)                                  #Moves the pointer to line 1

    for record in file_input:                           #Iterates through all 
        row = record.split(",")
        if row[3] == "Male":
            males_counter += 1
        elif row[3] == "Female":
            females_counter += 1

    print(f"There are {males_counter} guys.")
    time.sleep(1)
    print(f"There are {females_counter} girls.")
    time.sleep(1)

    males_counter = int(males_counter)
    females_counter = int(females_counter)
    gender_difference = abs(males_counter - females_counter)

    if males_counter > females_counter:
        print(f"There are {gender_difference} more guys than gals")
    elif females_counter > males_counter:
        print(f"There are {gender_difference} more gals than guys")
    time.sleep(1)


if __name__ == '__main__':
    main()



