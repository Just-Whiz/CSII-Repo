import time                                                     

def main():                              
    time.sleep(1)
    while True:
            try:
                l, h, t, zip1, zip2  = [(float(x)) for x in input("Enter values: ").split(",")]                                                                                                
                postsize = getsize(l, h, t)                                                                 
                zone1, zone2  = (getzone(zip1, zip2))                                                                   
                zonestravelled = float(int(abs(zone1 - zone2)))
                time.sleep(1)
                totalpostcost = postcost(postsize, zonestravelled)
                if totalpostcost == None:
                    print("Unmailable")
                else:
                    print(totalpostcost)
            except ValueError:
                print("Re-enter the values in a format seperated by commas")                                               


def getsize(l, h, t):
    if (l >= 3.5 and l <= 4.25) or (h >= 3.5 and h <= 6) or (t >= 0.007 and t <= 0.016): postclass = 1
    elif (l >= 4.25 and l <= 6) or (h >= 6 and h <= 11.5) or (t >= 0.007 and t <= 0.15): postclass = 2
    elif (l >= 3.5 and l <= 6.125) or (h >= 5 and h <= 11.5) or (t >= 0.25 and t <= 0.5): postclass = 3
    elif (l >= 6.125 and l <= 24) or (h >= 11 and h <= 18) or (t >= 0.25 and t <= 0.5): postclass = 4
    elif (l + h*2 + t*2) <= 84: postclass = 5
    elif 84 >= (l + h*2 + t*2 <= 130): postclass = 6
    else: postclass = None
    return postclass


def getzone(zip1, zip2):
    if (zip >= 1) and (zip1 <= 6999): zone = 1
    elif (zip >= 7000) and (zip1 <= 19999): zone = 2
    elif (zip >= 20000) and (zip1 <= 35999): zone = 3 
    elif (zip >= 36000) and (zip1 <= 62999): zone = 4
    elif (zip1 >= 63000) and (zip1 <= 84999): zone = 5
    elif (zip1 >= 85000) and (zip1 <= 99999): zone = 6

def postcost(postclass, zonestravelled):
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