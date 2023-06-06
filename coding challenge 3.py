# Nihaal Sidhu sidhuns@mail.uc.edu
# Coding Challenge 3
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()


'''
I made my code more efficent by creating a set of words "wordCR" from the list
of words which decreased look up time. My implementation then uses the 
intersection method of sets to improve efficency. 
'''

from itertools import permutations

wordCR = set(words)

def allsteps(word):
    """
    >>> allsteps("APPLE")
    ['ALEPPO', 'APPEAL', 'CAPPLE', 'DAPPLE', 'LAPPED', 'LAPPER', 'LAPPET', 'PALPED', 'PAPULE', 'RAPPEL', 'UPLEAP']
    
    >>> allsteps("UC")
    ['CUB', 'CUD', 'CUE', 'CUM', 'CUP', 'CUR', 'CUT', 'LUC', 'UCA']
    
    >>> allsteps("BEARCAT")
    ['ACERBATE', 'BACTERIA', 'BRACCATE', 'BRACTEAL', 'CARTABLE', 'SCABRATE']
    """
    steppers = set()
    # for loop that goes through entire alphabet 
    for L in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        # Creates all possible anagrams and checks if its in list
        anagrams = set(["".join(p) for p in permutations(word + L)])
        steppers.update(anagrams.intersection(wordCR))
    
    # Removes input word if in set and returns
    steppers.discard(word)
    return sorted(list(steppers))

#importing doctests
import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)

