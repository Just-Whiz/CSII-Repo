import csv

def main():
   
    """ doc """

def test_function():
    """
    Test function to see if I can 
    read the header of the csv file
    """
    with open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r') as infile:
        reader = csv.reader(infile, delimiter=",")
        header = next(reader)
        for row in reader: 
            student_first_name = row[0]
            student_last_name = row[1]
            student_year = row[2]
            student_grade = row[3]


#def get_something1():
    #file_input = open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\PostOffice\\gcds_data3.csv")

#if __name__ == '__main__':
    #main()