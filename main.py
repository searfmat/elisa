import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
import math

validPos = 0.075
validNeg = 0.15

def posControl(PC1, PC2):
    return ((PC1 + PC2) / 2)

def negControl(NC1, NC2):
    return((NC1 + NC2) / 2)

def isValid(PCX, NCX):
    if((PCX - NCX) > validPos and (NCX <= validNeg)):
        return True
    else: 
        return False

def calcSP(OD, NCX, PCX):
    return((OD - NCX)/(PCX - NCX))

def calcTiter(SP):
    if(SP <= 0):
        return 0

    x = 1.09 * math.log(SP) + 3.36
    return pow(10,x)

def readCSV():
    csvList = []
    ifile  = open('csv/test.csv', "r")
    read = csv.reader(ifile)
    for row in read:

        for i in row:
            if(any(map(str.isdigit, i))):
                csvList.append(float(i))

    return csvList
    


def main():
    vals = readCSV()
    ods = []
    titerGroup = []
    

    PC = posControl(vals[24], vals[36])
    NC = negControl(vals[0], vals[12])

    #Suppressed warnings
    #if((isValid(PC, NC)) == False):
    #    print("ERROR: Invalid PCX and NCX values")
    #    exit()

    for k in range(len(vals)):
        if(k == 0 or k == 12 or k == 24 or k == 36):
            continue
        else:
            ods.append(vals[k])

    for j in ods:
        titer = calcTiter(calcSP(j, NC, PC))
        if(titer == 0):
            titerGroup.append(0)
        elif(titer < 1000):
            titerGroup.append(1)
        elif(titer < 2000):
            titerGroup.append(2)
        elif(titer < 3000):
            titerGroup.append(3)
        elif(titer < 4000):
            titerGroup.append(4)
        elif(titer < 5000):
            titerGroup.append(5)
        elif(titer < 6000):
            titerGroup.append(6)
        elif(titer < 7000):
            titerGroup.append(7)
        elif(titer < 8000):
            titerGroup.append(8)
        elif(titer < 9000):
            titerGroup.append(9)
        else:
            titerGroup.append(10)    

    r = (0, 18)
    bins = 18  

    plt.hist(titerGroup, bins, r, color = 'blue',
            histtype = 'bar', rwidth = 0.8)

    plt.xlabel('Titer Groups')

    plt.ylabel('Count')
    plt.title('PC TURKEY SERA - REO')

    ax = plt.subplot()

    #I know, I know. But theres no support for range()
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
    ax.set_xticklabels('')

    ax.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5],      minor=True)
    ax.set_xticklabels(['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'], minor=True)
    plt.show()

    print("Done")


main()