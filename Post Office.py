#Project name: GCDS Rust Removal AKA the GCDS Post office algorithm
#Started: 9/18/23
#Ended: 
#Current version: 0.25
#Challenges: making the data entry user-friendly (although should be "to-spec"), 
#Working on: pseudocode and getting some necessary variables down

import time

# Defining main function
# Asks the user for 
def main():
    print("Welcome to the GCDS Post Office. Enter your data below.")
    time.sleep(1)
    l = float(input("Enter length: "))
    h = float(input("Enter height: "))
    t = float(input("Enter thickness: "))
    zip1 = float(input("Enter your starting zip: "))
    zip2 = float(input("Enter your ending zip: "))
    postsize = getsize(l, h, t)
    zone1 = getzone(zip1, zip2)
    print(postsize, zone1)

#getsize takes in 3 parameters (length, height, and thickness [l, h, & t])
#If the parameters are between certain numbers and all of them meet the parameters, then the variable "postclass" will be changed.
#Once the calculations are performed, the function finishes by returning the value of postclass.

def getsize(l, h, t):
    if (l >= 3.5 or l <= 4.25) and (h >= 3.5 or h <= 6) and (t >= 0.007 or t <= 0.016): postclass = "Regular Post Card"                
    elif (l >= 4.25 or l <= 6) and (h >= 6 or h <= 11.5) and (t >= 0.007 or t <= 0.15): postclass = "Large Post Card"
    elif (l >= 3.5 or l <= 6.125) and (h >= 5 or h <= 11.5) and (t >= 0.25 or t <= 0.5): postclass = "Envelope"
    elif (l >= 6.125 or l <= 24) and (h >= 11 or h <= 18) and (t >= 0.25 or t <= 0.5): postclass = "Large Envelope"
    #elif (l > 6.125 and h > 18  and t > 0.5): [working on the next set of parameters]
    else:
        postclass = "Unmailable"
    return postclass

#getfinalzone takes in 2 parameters (zip1 and zip2 [zip1 & zip2])
#If 

def getzone(zip1, zip2):
    if (zip1 or zip2 >= 1) and (zip1 or zip2 <= 6999): zone1 = 1
    elif (zip1 or zip2 >= 7000) and (zip1 or zip2 <= 19999): zone1 = 2
    elif (zip1 or zip2 >= 20000) and (zip1 or zip2 <= 35999): zone1 = 3
    elif (zip1 or zip2 >= 36000) and (zip1 or zip2 <= 62999): zone1 = 4
    elif (zip1 or zip2 >= 63000) and (zip1 or zip2 <= 84999): zone1 = 5
    elif (zip1 or zip2 >= 85000) and (zip1 or zip2 <= 99999): zone1 = 6
    return zone1
    


# Using the special variable 
# __name__
if __name__=="__main__":
    main()