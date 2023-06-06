#Nihaal Sidhu 
#imports
import scipy
import numpy as np
from random import random

rand_balls = np.arange(1,1000,1)
MaxBin = []
for N in rand_balls:
    bins = np.zeros(N)
    numBins = 0
    for b in range(N):
        bins[int(N * random())] +=1
    for i in bins:
        if i == 0:
            numBins += 1

    MaxBin.append(numBins)


#plot for lab
import matplotlib.pyplot as plt
plt.plot(rand_balls, MaxBin)
plt.show()
result = scipy.stats.linregress(rand_balls,MaxBin)
print ("SciPy Linear Regression Solution ")
print("Slope: ",result.slope * 2 )
print("Intercept: ",result.intercept)
print("Rvalue: ", result.rvalue)

