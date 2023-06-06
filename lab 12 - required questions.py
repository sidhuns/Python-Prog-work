#Nihaal Sidhu 
#RQ1
class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """
    def __init__(self, c):
        self.value = c
        self.ranger = len(c)
    
    def __iter__(self):
        self.blue = 0
        return self
        
    def __next__(self):
        if self.blue < self.ranger:
            john = self.value[self.blue]
            self.blue += 1
            return ("Give me an " + john)
        else:
            raise StopIteration
    
    


#RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    def __init__(self, c):
        self.value = c
        print(self.value)
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.value > 0:
            self.value -= 1
            return self.value
        else:
            raise StopIteration
    
    
    
    


##############
# Generators #
##############

# RQ3
def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = evens()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    i = 2
    while True:
        yield i 
        i += 2
#RQ4
def naturals():
    i = 1
    while True:
        yield i
        i += 1

def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    for i in s:
        yield i * k
# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    i = n
    while i >= 0:
        yield i
        i -= 1
    


# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    j = n
    print(n)
    while j != 1:
        if j % 2 ==  0:
            j = int(j / 2)
            yield j
        else:
            j = int((j* 3) + 1)
            yield j
            
    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)