## Lab 5: Required Questions - Dictionaries  ##
#Nihaal Sidhu
# used the lab sheet and learned what .keys() is
# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    new = dict1 | dict2
    return new

# RQ2
def counter(message):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal 
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    temp = message.split()
    check = {} 
    for i in temp:  
        if i not in check:  
            check[i] = 1  
        else: check[i] += 1 
    return check 
# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> d2= replace_all(d, 3, 'poof')
    >>> d2 == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    for i in d:
        if d[i] == x:
            d[i] = y
            
    return d

# RQ4
def sumdicts(lst):
   """ 
   Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And 
   if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
   as the value mapped for that key
   >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
   >>> d == {'a': 140,'b': 88, 'c': 100, 'd': 19}
   True
   """
   temp = {}
   for i in lst:
       for j in i.keys():
           temp[j] = temp.get(j, 0) + i[j]
#the loop iterates through each dict, then the second loop
#iterates through the keys in each dict, we create a new dict to hold each value, and use .get to get each value
#from the key(j), if the key doesn't exist it defaults as 0. this is added to the dict at j.
   return temp

#RQ5


def middle_tweet(table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string which has length in middle value of the 5.
    Returns a string that is a random sentence of median length starting with word, 
    and choosing successors from table. It is difficult to write a doctest for this function, 
    since it is randomized. But my experiments showed that with 5 random samples you should usually
    get a tweet that is roughly ordinary size sentence (6-10 words)
     """
    def construct_tweet(word, table):
        """Returns a string that is a random sentence starting with word, and choosing successors from table.
        """
        import random
        result = ' '
        while word not in ['.', '!', '?']:
            result += word + ' '
            word = random.choice(table[word])
        return result + word

    def random_tweet(table):
        import random
        return construct_tweet(random.choice(table['.']), table)

    T1 = random_tweet(table)
    T2 = random_tweet(table)
    T3 = random_tweet(table)
    T4 = random_tweet(table)
    T5 = random_tweet(table)

    Llist = [len(T1),len(T2),len(T3),len(T4),len(T5)]
    
    middleT = Llist.median
    
    print(middleT)
    
    return 1
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)