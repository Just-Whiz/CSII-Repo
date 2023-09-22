#Project name: GCDS Rust Removal AKA the GCDS Post office algorithm
#Started: 9/18/23
#Ended: 
#Current version: 0.21
#Challenges: making the data entry user-friendly (although should be "to-spec"), 
#Working on: pseudocode and getting some necessary variables down

import time


l = ""
w = ""
h = ""
zip2 = ""
zip1 = ""

def getsize(l, h, t):
    #Function takes in 3 parameters (length, height, and thickness [l, h, & t])
    #If the parameters are between certain numbers and all of them meet the parameters, then the variable "postclass" will be changed dependent on the parameter given.
    #Once the calculations are performed, the function finishes by returning the value of postclass, which was set by the parameters
    if (l >= 3.5 or l <= 4.25) and (h >= 3.5 or h <= 6) and (t >= 0.007 or t <= 0.016): postclass = "Regular Post Card"                
    elif (l >= 4.25 or l <= 6) and (h >= 6 or h <= 11.5) and (t >= 0.007 or t <= 0.15): postclass = "Large Post Card"
    elif (l >= 3.5 or l <= 6.125) and (h >= 5 or h <= 11.5) and (t >= 0.25 or t <= 0.5): postclass = "Envelope"
    elif (l >= 6.125 or l <= 24) and (h >= 11 or h <= 18) and (t >= 0.25 or t <= 0.5): postclass = "Large Envelope"
    #elif (l > 6.125 and h > 18  and t > 0.5): [working on the next set of parameters]
    return postclass 

def getzone(startZone):
    if zip1 >= 00001 or zip1 <= 06999:
        startZone = 1
    elif zip1 > =

    return startZone