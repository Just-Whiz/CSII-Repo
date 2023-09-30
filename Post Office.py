import time                                                     

def main():                              
    time.sleep(1)
    while True:
            try:
                length, height, thickness, zip1, zip2  = [(float(x)) for x in input("Enter values: ").split(",")]                                                                                                
                postsize = get_size(length, height, thickness)                                                                 
                zone1list = (get_zone(zip1, zip2)) 
                zone1 = zone1list[0]   
                zone2list = (get_zone(zip1, zip2))
                zone2 = zone1list[0]  
                zonestravelled = float(int(abs(zone1 - zone2)))
                time.sleep(1)
                totalpostcost = post_cost(postsize, zonestravelled)
                if totalpostcost == None:
                    print("Unmailable")
                else:
                    print(totalpostcost)
            except ValueError:
                print("Re-enter the values in a format seperated by commas")                                               


def get_size(l, h, t):
    length = l
    height = h
    thickness = t
    if ((l >= 3.5 and l <= 4.25) or (h >= 3.5 and h <= 6) or 
        (t >= 0.007 and t <= 0.016)): 
         postclass = 1
    elif ((l >= 4.25 and l <= 6) or (h >= 6 and h <= 11.5) 
         or (t >= 0.007 and t <= 0.15)): 
         postclass = 2
    elif ((l >= 3.5 and l <= 6.125) or (h >= 5 and h <= 11.5) 
         or (t >= 0.25 and t <= 0.5)): 
         postclass = 3
    elif ((l >= 6.125 and l <= 24) or (h >= 11 and h <= 18)
         or (t >= 0.25 and t <= 0.5)): 
         postclass = 4
    elif (l + h*2 + t*2) <= 84: postclass = 5
    elif 84 >= (l + h*2 + t*2 <= 130): postclass = 6
    else: postclass = None
    return postclass

def get_zone(zip1, zip2):
        zipfrom = zip1
        zipto = zip2
        if (zipfrom >= 1) and (zipfrom <= 6999): 
            zone1 = 1
            if (zipto >= 1) and (zipto <= 6999):
                zone2 = 1
        elif (zipfrom >= 7000) and (zipfrom <= 19999): 
            zone = 2
            if (zipto >= 7000) and (zipto <= 19999):
                 zone2 = 2
        elif (zipfrom >= 20000) and (zipfrom <= 35999):
             zone1 = 3
             if (zipto >= 20000) and (zipto <= 35999):
                  zone2 = 3
        elif (zipfrom >= 36000) and (zipfrom <= 62999): 
             zone1 = 4
             if (zipto >= 36000) and (zipto <= 62999):
                  zone2 = 4
        elif (zipfrom >= 63000) and (zipfrom <= 84999): 
             zone1 = 5
             if (zipto >= 63000) and (zipto <= 84999): 
                  zone2 = 5
        elif (zipfrom >= 85000) and (zipfrom <= 99999): 
             zone1 = 6
             if (zipto >= 85000) and (zipto <= 99999): 
                zone2 = 6
        return [zone1, zone2]

def post_cost(postclass, zonestravelled):
    if postclass == 1: postcost = (0.03 * zonestravelled) + 0.20
    elif postclass == 2: postcost = (0.03 * zonestravelled) + 0.37
    elif postclass == 3: postcost = (0.04 * zonestravelled) + 0.37
    elif postclass == 4: postcost = (0.05 * zonestravelled) + 0.60
    elif postclass == 5: postcost = (0.25 * zonestravelled) + 2.95
    elif postclass == 6: postcost = (0.35 * zonestravelled) + 3.95
    elif postclass == 7: postcost = None
    return postcost

# Using the special variable 
# __name__
if __name__=="__main__":
    main()