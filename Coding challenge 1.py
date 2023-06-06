"""
Created on Sun Jan 29 16:43:08 2023

@author: Nihaal Sidhu

"""
## Partial credit will be given for code that passes the two given doctests. 
## For full credit on HW1 you should test your solutions to egypt(103,104) and  egypt(123,124)
## These are more difficult and may require you to develop faster, more efficient code.
## Hint: you may consider using code for gcd function for greatest common divisor:
## https://www.geeksforgeeks.org/gcd-in-python/
import math
def egypt(n,d):
    """
    >>> egypt(3,4)
    '1/2 + 1/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12'
    
    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424'
    """
#Array containing the element of the denominator of the unit fraction
    denomarr = []
    temp = 0
#This while loop calculates the denom of the unit fraction, the if statement is to avoid overflow
#then adds denominator to denomarr, ends with changing values for next iteration.
    while n != 0:
        
        if d > 10000000000:
            temp = d // n
           
        else:
            temp = math.ceil(d / n)
    
        denomarr.append(temp)
    
        n = (temp * n) - d
        d = (d * temp)
    
#print results, use loop to iterate through array and if statement for spacing
    i = 0
    print("'", end = "")
    for i in (range(len(denomarr))):
        
        if i != (len(denomarr) - 1):
            print("1/{0} +".format(denomarr[i]), end = " ")
            
        else:
            print("1/{0}".format(denomarr[i]), end = "")
            
    print("'", end = "")
    
#doctesting
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
        
    

