# Program Name: ChrisSuyFileIO.py
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 10/6/23
# I pledge my honor

import csv
import time

def main():
   
    """ doc """
    file_input = open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r')

    file_input.readline()                       #skip first line of header info
    answer = "Y"
    go = True

   
    while go is True:
        print('''Menu: Enter Choice or 'Q' to (Q)uit:
1) Print all students at school
2) Print all students in grade 12
3) Compare the amount of boys versus girls
''')
        time.sleep(1)
        answer = input("Enter your input here: ")

        if answer == "1":
            display_all(file_input)
            time.sleep(1)
        elif answer == "2":
            count_seniors(file_input)
            time.sleep(1)
        elif answer == "3":
            compare_genders(file_input)





def display_all(file_input):

    """
    This function displays all the students/all the data in the given CSV file.
    It first opens the CSV file (gcds_data3.csv), assigns a variable as a reader (reader), defines the
    header (header), and then moves the reader past it, because it is the first line of the document.
    It assigns variable names to each row, and prints all the data present in each of those rows.
    Each variable is stylized with the title present for each of the rows in the file.
    Ex: student_last_name is each student's last name.
    """

    file_input.seek(1)

    for record in file_input: 
        row = record.split(",")
        time.sleep(0.00000000001)
        print(row[1], row[2], row[3], row[4], row[5])

def count_seniors(file_input):
    """
    This function displays all the seniors' names that currently go to GCDS. 

    By taking file_input as a variable, (as defined in the main), this function is able to iterate through all the kids (rows)
    in the csv file that the variable is attached to (gcds_data3.csv), and single out the first and last kids of the 
    kids who are in that grade level. After each name is listed, the iteration pauses for a fraction of a second before
    continuing. 

    record - Denotes the columns 
    kid - Denotes the columns and rows and splits them them by the delimiter (in this case, a comma ",")
    """
    
    file_input.seek(1)                                     #moves pointer to line 1

    for record in file_input:
        kid = record.split(",")
        if kid[2] == "Grade 12":
            time.sleep(0.01)
            print(kid[1] + " " + kid[0])
        time.sleep(1)

def compare_genders(file_input):
    """
    This function counts the amount of girls and boys, and finds who has more numbers in terms of gender.

    By taking file_input as a variable, (as defined in the main), this function is able to iterate through all the rows
    in the csv file that the variable is attached to (gcds_data3.csv), and singles out the third row as the row 

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

    print(f"There are {males_counter} guys versus {females_counter} girls")
    if males_counter > females_counter:
        print("there are more guys")
    elif females_counter > males_counter:
        print("there are more gals")
    time.sleep(1)

if __name__ == '__main__':
    main()