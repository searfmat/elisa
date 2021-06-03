import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv

validPos = 0.075
validNeg = 0.15


def posControl(PC1, PC2):
    return
def negControl(NC1, NC2):
    return
def isValidPos(PCX):
    return
def isValidNeg(NCX):
    return
def calcSP():
    return
def calcTiter():
    return

def readCSV():
    csvList = []
    ifile  = open('csv/test.csv', "r")
    read = csv.reader(ifile)
    for row in read:

        for i in row:
            if(any(map(str.isdigit, i))):
                csvList.append(float(i))

    return csvList
    


print(readCSV())
# frequencies
ages = [3, 5, 3, 3]
  

range = (0, 18)
bins = 18  

plt.hist(ages, bins, range, color = 'blue',
        histtype = 'bar', rwidth = 0.8)

plt.xlabel('Titer Groups')

plt.ylabel('Count')
plt.title('PC TURKEY SERA - REO')

ax = plt.subplot()

#I know, I know. But theres no support for range()
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
ax.set_xticklabels('')

ax.set_xticks([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5],      minor=True)
ax.set_xticklabels(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'], minor=True)
plt.show()

print("done")


