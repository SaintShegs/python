from itertools import groupby
from collections import Counter
def myFunc(x):
    return x+5



def anotherFunc(x):
    return x//5


no_of_socks=9

colOfSocks=[10,20,30,10,10,30,50,10,20]

# c=Counter(colOfSocks)

# print[[k,]*v for k,v in c.items()]



colOfSocks.sort()
sort=[list(j) for i,j in groupby(colOfSocks)]
print(sort)
print(len(sort))
    

