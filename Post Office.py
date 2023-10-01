import time                                                     

def main():                              
    time.sleep(1)
    while True:
            try:
                length, height, thickness, zip1, zip2  = [(float(x)) for x in input("Enter values: ").split(",")]                                                                                                
                postsize = get_size(length, height, thickness)                                                                 
                zonelist = get_zone(zip1, zip2) 
                startzone = zonelist[0]
                endzone = zonelist[1]
                zonestravelled = float(int(abs(startzone - endzone)))
                totalpostcost = post_cost(postsize, zonestravelled)
                if totalpostcost == None:
                    print("Unmailable")
                else:
                    print('%.2f'%totalpostcost)
            except ValueError:
                print("Re-enter the values in a format seperated by commas")                                               


def get_size(l, h, t):
    """
    Returns a package type number based on the postage values given.

    The 
    """
    length = l
    height = h
    thickness = t
    if ((l >= 3.5 and l <= 4.25) and (h >= 3.5 and h <= 6) 
         and (t >= 0.007 and t <= 0.016)): 
         postclass = 1
    elif ((l >= 4.25 and l <= 6) and (h >= 6 and h <= 11.5) 
         and (t >= 0.007 and t <= 0.15)): 
         postclass = 2
    elif ((l >= 3.5 and l <= 6.125) and (h >= 5 and h <= 11.5) 
         and (t >= 0.25 and t <= 0.5)): 
         postclass = 3
    elif ((l >= 6.125 and l <= 24) and (h >= 11 and h <= 18)
         and (t >= 0.25 and t <= 0.5)): 
         postclass = 4
    elif (l + h*2 + t*2) <= 84: 
          postclass = 5
    elif 84 >= (l + h*2 + t*2 <= 130): 
          postclass = 6
    else: 
          postclass = None
    return postclass

def get_zone(zip1, zip2):
        """
        Returns two different zone values based on the two zips fed in by the user.

        The first zipcode is identified as zip1 and the second zipcode is called zip2. 
        The algorithm uses both to determine the zone identification number of each zipcode.
        Starting from zip1 (changed to zipfrom for readability) to zip2 (changed to zipto), 
        it assigns it a variable for identification and then proceeds to return both values 
        in a list form, because two values cannot be returned at a time
        """
        zipfrom = zip1                                                                                          # zip1's value identified as variable zipfrom's value
        zipto = zip2                                                                                            # zip2's value identified as variable zipto's value
        if (zipfrom >= 1) and (zipfrom <= 6999): zone1 = 1
        elif (zipfrom >= 7000) and (zipfrom <= 19999): zone1 = 2
        elif (zipfrom >= 20000) and (zipfrom <= 35999): zone1 = 3                                               # If the parameter zipfrom (zip1) is within 2 values, assign
        elif (zipfrom >= 36000) and (zipfrom <= 62999): zone1 = 4                                               # zone1 (the variable to be returned) to a value between
        elif (zipfrom >= 63000) and (zipfrom <= 84999): zone1 = 5                                               # 1-6
        elif (zipfrom >= 85000) and (zipfrom <= 99999): zone1 = 6 
        else:                                                                                                   # If the above conditions aren't met, fall back to 
            zone1 = "Unreachable"                                                                               # to an unreachable error message
        if (zipto >= 85000) and (zipto <= 99999): zone2 = 6
        elif (zipto >= 63000) and (zipto <= 84999): zone2 = 5
        elif (zipto >= 36000) and (zipto <= 62999): zone2 = 4                                                   # If the parameter zipto (zip2) is within 2 values, assign
        elif (zipto >= 20000) and (zipto <= 35999): zone2 = 3                                                   # zone2 (the second variable)        
        elif (zipto >= 7000) and (zipto <= 19999): zone2 = 2
        elif (zipto >= 1) and (zipto <= 6999): zone2 = 1
        else:
                zone2 = "Unreachable"                                                                           # Since two variables can't be returned at a time, the variables
        return [zone1, zone2]                                                                                   # are stored in a list on the function's return (or end)
            
def post_cost(postclass, zonestravelled):
    """

    """
    if postclass == 1: postcost = 0.20 + (0.03 * float(zonestravelled))
    elif postclass == 2: postcost = 0.37 + (0.03 * float(zonestravelled))
    elif postclass == 3: postcost = 0.37 + (0.04 * float(zonestravelled))
    elif postclass == 4: postcost = 0.60 + (0.05 * float(zonestravelled))
    elif postclass == 5: postcost = 2.95 + (0.25 * float(zonestravelled))
    elif postclass == 6: postcost = 3.95 + (0.35 * float(zonestravelled))
    else:
          postcost = None
    return postcost

# Using the special variable 
# __name__
if __name__=="__main__":
    main()