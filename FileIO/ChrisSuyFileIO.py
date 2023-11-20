# Program Name: GCDS Rust Removal AKA the GCDS Post Office
# Student Name: Chris Suy
# Course: CS II
# Instructor: Mr. Campbell
# Date: 10/6/23
# I pledge my honor

import csv
import time

print("hello")

def main():
   
    """ doc """
    file_input = open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r')

    file_input.readline()                       #skip first line of header info
    answer = "Y"
    go = True

   
    while go is True:
        print('''
              Menu: Enter Choice or 'Q' to (Q)uit:")
1) Print All Students at School")
2) Print All Students in Grade 12"
''')
        time.sleep(1)
        answer = input("Enter your input here: ")

        if answer == "1":
            display_all(file_input)
        elif answer == "2":
            count_seniors(file_input)
        elif answer == "3":
            try:
                first_name = input("Enter your first name")
                last_name = 

        


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
        student_last_name = row[0]
        student_first_name = row[1]
        student_grade = row[2]
        student_gender = row[3]
        student_address = row[4]
        student_state = row[5]
        print(student_first_name, student_last_name, student_grade, student_gender, student_address, student_state)

def count_seniors(file_input):
    """"""

if __name__ == '__main__':
    main()