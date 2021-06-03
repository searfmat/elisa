import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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




# frequencies
ages = [3, 5, 3, 3]
  
    # setting the ranges and no. of intervals
range = (0, 18)
bins = 18  
  
    # plotting a histogram
plt.hist(ages, bins, range, color = 'blue',
        histtype = 'bar', rwidth = 0.8)
  
    # x-axis label
plt.xlabel('Titer Groups')
    # frequency label
plt.ylabel('Count')
    # plot title
plt.title('PC TURKEY SERA - REO')

ax = plt.subplot()

#I know, I know. But theres no support for range()
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
    # function to show the plot
ax.set_xticklabels('')

# Customize minor tick labels
ax.set_xticks([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5],      minor=True)
ax.set_xticklabels(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'], minor=True)
plt.show()

print("done")


