# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:57:32 2023

@author: Nihaal Sidhu
Help from the lab 4 sheet
"""

##Lab04 Required Questions ##

#########
# Lists #
#########

# RQ1
def cascade(lst):
    """Returns the cascade of the given list running forward and back.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    john = lst
       
    jack = []
    i = 0
    while i < len(lst):
         jack = [lst[i]] + jack
         i += 1
        
    jared = john + jack 
       
    return jared


# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    randy = []
    john = []
    for aaron in seq:
        randy = randy + [fn(aaron)] 
        
    for alpaca in randy:
        john = john + [fn(alpaca)]
        
    return john

#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    randall = []
    for elroy in seq:
         if pred(elroy):
             thors = 2
             
         else:
             randall += [elroy]
             
    return randall

#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    randall = []
    for i in range(n):
         if pred(i):
             randall += [i]
             
    return randall

#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    if bool(lst):
        if type(lst[0]) == list:
            return flatten(*lst[:1]) + flatten(lst[1:])
        
        return lst[:1] + flatten(lst[1:])
    
    else:  
        return lst


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)