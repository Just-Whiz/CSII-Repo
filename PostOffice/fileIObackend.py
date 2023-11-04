import csv

def main(): 
    """
    documentation here
    """
    file_input = open("c:\\Users\gordie.campbell\\Documents\\GitHub\\CS2_Materials\\Labs\\gcds_data2.csv")

    file_input.readline() #skip first line of header info
    answer = "Y"
    go = True

    print("menu: Enter Choice or 'Q' to (Q)uit.")
    print("1) Print All Students in Grade 12")

    while go is True:
        if answer == "1":
            check_seniors(file_input)
        elif answer == "Q":
            go = False
            print("bye")
            return
        
        answer = input("Enter choice or 'Q' to quit")

        def check_seniors(file_in):
            """
            documentation here
            """

            file_in.seek(1) #move pointer to line 1

            for record in file_in: 
                kid = record.split(",")
                if kid[3] == "12":
                    print(kid[0] + "" + kid[2])
        


if __name__ == '__main__':
    main()