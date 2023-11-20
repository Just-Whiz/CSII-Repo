# Program Name: GCDS Rust Removal AKA the GCDS Post Office
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 10/6/23
# I pledge my honor

import csv
import time


def main():
    """"""
    file_input = open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r')

    file_input.readline()                       #skip first line of header info
    answer = "Y"
    go = True

    #This code runs the options menu
    while go is True:
            answer = input('''
Enter your input here                           
                           ''')                 #Asks the user for their selection input
            if answer == "1":
                display_all()
            elif answer == "2":
                compare_genders()
            elif answer == "3":
                count_seniors()
            elif answer == "Q":
                go = False
                print("bye")
                return

def display_all():
    """
    This function displays all the students/all the data in the given CSV file.
    It first opens the CSV file (gcds_data3.csv), assigns a variable as a reader (reader), and
    where the header is
    It assigns variable names to each row, and prints all the data present in each of those rows.
    Each variable is stylized with the title present for each of the rows in the file.
    Ex: student_last_name is each student's last name.
    """
    with open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r') as infile:
        reader = csv.reader(infile, delimiter=",")      #Defines the reader that will "read" in the CSV data
        header = next(reader)                           #Defines the variable that is the header
        for row in reader: 
            student_last_name = row[0]
            student_first_name = row[1]
            student_grade = row[2]
            student_gender = row[3]
            student_address = row[4]
            student_state = row[5]
            print(student_first_name, student_last_name, student_grade, student_gender, student_address, student_state)

def compare_genders():
    with open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r') as infile:
        reader = csv.reader(infile, delimiter=",")
        header = next(reader)
        row_count = sum(1 for row in reader)
    return row_count

def get_last_names():
    return sorted

def get_student():

    return student

def count_seniors(file_in):
    """"""
    file_in.seek(1)                                     #move pointer to line 1

    for record in file_in:
        kid = record.split(",")
        if kid[3] == "12":
            print(kid[0] + " " + kid[2])

if __name__ == "__main__":
    main()