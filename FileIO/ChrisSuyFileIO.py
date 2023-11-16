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
=-=
]file_input = open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r')
    file_input.readline()                       #skip first line of header info
    go = True

    #This code runs the options menu
    while go is True:
            answer = input('''What would you like to do?
1)
2)
3)
4)
5)
Enter your input here: ''')                 #Asks the user for their selection input
            if answer == "1":
                 print_all_kids()
                 time.sleep(1)
            elif answer == "2":
                print("placeholder")
                time.sleep(1)
            elif answer == "3":
                print("placeholder")
                time.sleep(1)
            elif answer == "Q":
                go = False
                print("bye")
                return
             
def print_all_kids():
     with open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r')