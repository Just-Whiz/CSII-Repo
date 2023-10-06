import time                                                     

def main():                                                                                                   # The bones of the project that calls all functions and uses them
    """
    Guides and marks the beginning of the project's code. 

    This main() first gets the length, height, thickness, zip1, & zip2
    variables through an input statement that can take 5 inputs for the
    purpose of "postage pricing". If the user inputs the data in an invalid format, the program spits out an 
    error message and tries again to get valid data. When done, it processes
    all variables through the functions get_size(), get_zone(), and then
    calculates the total cost (as according to the spec) to present the 
    user a two decimal base 10 value equivlant to the shipping cost of the postage.
    """                              
    time.sleep(1)
    i = 0
    while i < 5:                                                                                                 # A forever loop that runs everything inside until the conditions inside are false
            try:                                                                                                # A loop that catches and handles the ValueError exception when inputs are formatted incorrectly
                length, height, thickness, zip1, zip2  = [(float(x)) for x in input("").split(",")]  # Input that takes 5 inputs for 5 variables in order, formatted by commas                                                                                              
                postsize = get_size(length, height, thickness)                                                  # Gets the size of the postage based on 3 variables, length, height, and thickness             
                zonelist = get_zone(zip1, zip2)                                                                 # Organizes the returned "listed" values of get_zone into a list, called zonelist
                startzone = zonelist[0]                                                                         # Makes the value of the starting zone (startzone) the 1st listed value in zonelist
                endzone = zonelist[1]                                                                           # Makes the value of the ending zone (endzone) the 2nd listed value in zonelist
                zonestravelled = float(int(abs(endzone - startzone)))                                           # Calculates the zones travelled (zonestravelled) as the floated, integer, absolute value of 
                totalpostcost = str(post_cost(postsize, zonestravelled)).lstrip("0")                                             # startzone - endzone. totalpostcost is determined by function post_cost with arguments postsize and zonestravelled
                if totalpostcost == None:                                                                       # If the total cost is None (nothing, essentially) then print unmailable
                    print("Unmailable")                                                                         # Prints the error message of the aforementioned
                else:                                                                                           # If the above conditions aren't met
                    print(locals())
                    print(totalpostcost)                                                                 # Prints the total cost of sending the postage to the 100th decimal value
            except ValueError:                                                                                  # If the formatting exception ValueError is sent out by Python
                print("Unmailable")                                                                             # Prints an error message asking for proper input         

def get_size(l, h, t):                                                                                          # Gets the size of the postage based on the parameters given
    """
    Returns a package/postage type based on a number value given.

    It first converts length, height, and thickness into style-spec readable
    values, l, h, and t for the purpose of legibility. If they fall into specific
    parameters defined by the values in the algorithm, it is assigned a number value
    specific to a postage class, 
    """
    length = l                                                                                                  # length's value identified as new variable l's value
    height = h                                                                                                  # height's value identified as new variable h's value
    thickness = t                                                                                               # thickness's value identified as new variable t's value
    if ((l >= 3.5 and l <= 4.25) and (h >= 3.5 and h <= 6)                                                      # If l is between these 2 values, and h is between these 2 values,
         and (t >= 0.007 and t <= 0.016)):                                                                      # and t is between these 2 values, assign postclass a value
         postclass = 1                                                                                          # Postclass 1 is the Post Card class
    elif ((l >= 4.25 and l <= 6) and (h >= 6 and h <= 11.5)                                                     # For lines 48, 51, 54, 57, and 59's documentation, refer to 
         and (t >= 0.007 and t <= 0.15)):                                                                       # lines 45-46 on what they do
         postclass = 2                                                                                          # Postclass 2 is the Large Post Card class
    elif ((l >= 3.5 and l <= 6.125) and (h >= 5 and h <= 11.5) 
         and (t >= 0.25 and t <= 0.5)):                                                             
         postclass = 3                                                                                          # Postclass 3 is the Envelope class
    elif ((l >= 6.125 and l <= 24) and (h >= 11 and h <= 18)                                                    
         and (t >= 0.25 and t <= 0.5)): 
         postclass = 4                                                                                          # Postclass 4 is the Large Envelope class
    elif (l >= 24) and (h >= 18) and (t >= 0.5) and (l + (t + h)) <= 84: 
          postclass = 5                                                                                         # Postclass 5 is the Package class
    elif (l + (h + t)) >= 84 and (l + (h + t)) <= 130: 
          postclass = 6                                                                                         # Postclass 6 is the Large Package class
    else:                                                                                                       # If the above parameters aren't met,
          postclass = None                                                                                      # return Postclass as None (essentially, make its 
    return postclass                                                                                            # value worth nothing in Python's "eyes")

def get_zone(zip1, zip2):                                                                                       # Gets the zones of the two zipcodes entered (zip1 and zip2)
        """                                                
        Returns two different zone values based on the two zipcodes fed in by the user.
                                                                                                                
        The first zipcode is identified as zip1 and the second zipcode is called zip2. 
        The algorithm uses both to determine the zone identification number of each zipcode.
        Starting from zip1 (changed to zipfrom for readability) to zip2 (changed to zipto), 
        it assigns it a variable for identification and then proceeds to return both values 
        in a list form, because two values cannot be returned at a time
        """
        zipfrom = zip1                                                                                          # zip1's value identified as new variable zipfrom's value
        zipto = zip2                                                                                            # zip2's value identified as new variable zipto's value
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
            
def post_cost(postclass, zonestravelled):                                                                       # Gets the postage class based on the type of postage 
    """
    Gets the postage class based on the type of postage and the zones it has travelled.

    The postage class is determined earlier by the get_size() function, and the zones 
    travelled is defined by the main() early on before calling this function. Based on this,
    the postcost is a set value for each seperate postclass plus a flat rate times the 
    amount of zones travelled. Otherwise, the value returned is None (or nothing), and it 
    assigns and returns postcost as the total amount to be paid. 
    """
    if postclass == 1: postcost = 0.20 + (0.03 * float(zonestravelled))                                         # If the postclass is equal to a certain value, set the postcost equal to a 
    elif postclass == 2: postcost = 0.37 + (0.03 * float(zonestravelled))                                       # a fixed amount + a distinct flat rate times the floated value of the 
    elif postclass == 3: postcost = 0.37 + (0.04 * float(zonestravelled))                                       # zonestravelled variable. This is repeated across the next 3 elif statements
    elif postclass == 4: postcost = 0.60 + (0.05 * float(zonestravelled))
    elif postclass == 5: postcost = 2.95 + (0.25 * float(zonestravelled))
    elif postclass == 6: postcost = 3.95 + (0.35 * float(zonestravelled))
    else:                                                                                                       # If the above conditions aren't met, fall back to 
          postcost = None                                                                                       # setting the postcost as None (a value meaning nothing(?))
    return postcost                                                                                             # Returns postcost's value based on the calculations done in the function

if __name__=="__main__":                                                                                        # Using the spicy, special variable 
    main()                                                                                                      # __name__

