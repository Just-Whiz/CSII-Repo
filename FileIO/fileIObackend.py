import csv

outfile = open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'w')
with open("C:\\Users\\csuy26\Desktop\\CSII-Repo\\FileIO\\gcds_data3.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    for row in reader: 
        student_first_name = row[0]
        student_last_name = row[1]
        student_year = row[2]
        student_grade = row[3]
        print(student_first_name, student_last_name, student_year, student_grade)
