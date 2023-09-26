#Project name: GCDS Rust Removal AKA the GCDS Post office algorithm
#Started: 9/18/23
#Ended: 
#Current version: 0.25
#Challenges: making the data entry user-friendly (although should be "to-spec"), 
#Working on: pseudocode and getting some necessary variables down

import time

# Defining main function
# Asks the user for their postage inputs and stores them in their corresponding variables
def main():
    print("Welcome to the GCDS Post Office. Enter your data below.")
    time.sleep(1)
    l = float(input("Enter length: "))
    h = float(input("Enter height: "))
    t = float(input("Enter thickness: "))
    zip1 = float(input("Enter your starting zip: "))
    zip2 = float(input("Enter your ending zip: "))
    postsize = getsize(l, h, t)
    zone1 = getzone1(zip1) 
    zone2 = getzone2(zip2)
    zonestravelled = float(int(abs(zone1 - zone2)))
    time.sleep(1)
    totalpostcost = postcost(postsize, zonestravelled)
    print(totalpostcost).print(locals())
    

#getsize is a simple algorithm that takes in 3 parameters (length, height, and thickness [l, h, & t])
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
        #Assigned when any item does not conform to the above requirements
    return postclass

#getfinalzone takes in 2 parameters (zip1 and zip2 [zip1 & zip2])
#If either zips are within certain parameters, then it'll assign them a zone within the integers of numbers they find themselves in

def getzone1(zip1):
    if (zip1 >= 1) and (zip1 <= 6999): zone1 = 1
    elif (zip1 >= 7000) and (zip1 <= 19999): zone1 = 2
    elif (zip1 >= 20000) and (zip1 <= 35999): zone1 = 3
    elif (zip1 >= 36000) and (zip1 <= 62999): zone1 = 4
    elif (zip1 >= 63000) and (zip1 <= 84999): zone1 = 5
    elif (zip1 >= 85000) and (zip1 <= 99999): zone1 = 6
    return zone1
#Returns the variable zone1 as the zone the starting zipcode is located in

#See the above description for the function below

def getzone2(zip2):
    if (zip2 >= 1) and (zip2 <= 6999): zone2 = 1
    elif (zip2 >= 7000) and (zip2 <= 19999): zone2 = 2
    elif (zip2 >= 20000) and (zip2 <= 35999): zone2 = 3
    elif (zip2 >= 36000) and (zip2 <= 62999): zone2 = 4
    elif (zip2 >= 63000) and (zip2 <= 84999): zone2 = 5
    elif (zip2 >= 85000) and (zip2 <= 99999): zone2 = 6
    return zone2
#Returns the variable zone2 as the zone the ending zipcode is located in

#postcost takes in 2 parameters (postclass & zonestravelled)
#If postclass is equal to a particular string value, the cost is equal to certain "tariff" times another set tariff per zones travelled

def postcost(postclass, zonestravelled):
    if postclass == "Regular Post Card": postcost == 0.20 + 0.03 * float(zonestravelled) 
    elif postclass == "Large Post Card": postcost == 0.37 + 0.03 * float(zonestravelled)
    elif postclass == "Envelope": postcost == 0.37 + 0.04 * float(zonestravelled)
    elif postclass == "Large Envelope": postcost == 0.60 + 0.05 * float(zonestravelled)
    elif postclass == "Package": postcost == 2.95 + 0.25 * float(zonestravelled)
    elif postclass == "Large Package": postcost == 3.95 + 0.35 * float(zonestravelled)
    else: 
        print("Unmailable")
        #Assigned if the data entered or postclass does not meet the above requirements
    return postcost
#Returns the variable postcost as the final total cost with all 5 inputs

# Using the special variable 
# __name__
if __name__=="__main__":
    main()