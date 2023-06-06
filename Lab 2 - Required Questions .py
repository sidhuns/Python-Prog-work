# CS2021 Lab 02 - Required Questions
## Modify this file by adding your salutation and code. 
## Once you pass all the doctests, then 
## you can then submit you program for credit. 

_author_ = "Nihaal Sidhu"
_credits_ = ["Module 2 lab sheet"]
_email_ = "sidhuns@mail.uc.edu" # Your email address

#  RQ1
"""
Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is 'Sunday'. 
Your function should return error message if the arguments to the function are not valid. 
"""
def day_name(n):
    """
    >>> day_name(3) 
    'Wednesday'
    >>> day_name(6) 
    'Saturday'
    >>> day_name(42)
    'Invalid argument'
    """
    day = "Sunday"
    if n == 0:
        print(day)
    elif n == 1:
        day = "'Monday'"
        print(day)
    elif n == 2:
        day = "'Tuesday'"
        print(day)
    elif n == 3:
        day = "'Wednesday'"
        print(day)
    elif n == 4:
        day = "'Thursday'"
        print(day)
    elif n == 5:
        day = "'Friday'"
        print(day)
    elif n == 6:
        day = "'Saturday'"
        print(day)
    else:
        print("'Invalid argument'")
    
    return
        

#  RQ2
def two_of_three(a, b, c):
    """Return value using only a one-line return statement.  The value should be the sum of two squares x*x + y*y, 
         where x and y are the two largest members of the set of. positive numbers a, b, and c.
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return ((a**2 + b**2 + c**2) - min(a,b,c)**2)
 


#  RQ3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    """
    john = 1
    biggest1= 1
    biggest2= 0
    for i in range(n):
        if n % john == 0:
            biggest2 = john
        if biggest1 < biggest2 and biggest2 != n:
            biggest1 = biggest2
        john = john + 1
        
        
    return biggest1
        
    
         

# RQ 4
def keeper(pred, n):
    """Print the numbers between 1 and n which satisfy the predicate pred.

    >>> keeper(lambda x: x%2 == 0, 15)
    2 4 6 8 10 12 14 
    >>> keeper(lambda x: x%7 == 0, 40)
    7 14 21 28 35 
    """
    
    john = pred
    j = 1
    for i in range(1,n + 1):
        
        if john(i):
            print(j, end = " ")
        j = j+ 1

    return 
    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)